"""채팅 답변 생성, Gemini 선택 호출, Redis 캐시, Supabase 로그 저장을 연결합니다."""

from __future__ import annotations

from dataclasses import dataclass

import httpx
from fastapi import HTTPException

from app.core.config import get_settings
from app.schemas.auth_schema import UserPublic
from app.schemas.chat_schema import ChatLogPublic, ChatRequest, ChatResponse
from app.services import redis_service


TABLE_NAME = "ex90_user_chat_logs"


@dataclass(frozen=True)
class AnswerResult:
    """AI 답변 생성 결과를 한 묶음으로 전달하기 위한 작은 데이터 클래스입니다."""

    answer: str
    provider: str
    model: str
    actual_api_called: bool


def table_url() -> str:
    """Supabase REST API에서 채팅 로그 테이블을 호출할 URL을 만듭니다."""

    return f"{get_settings().supabase_url}/rest/v1/{TABLE_NAME}"


def service_headers() -> dict[str, str]:
    """service role key로 Supabase REST API를 호출할 때 사용하는 헤더입니다.

    service role key는 RLS를 우회할 수 있는 서버 전용 key입니다.
    따라서 이 헤더는 FastAPI 서버 안에서만 사용하고 프론트엔드로 보내면 안 됩니다.
    """

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(status_code=500, detail="Supabase 환경변수를 확인하세요.")
    return {
        "apikey": settings.supabase_service_role_key,
        "Authorization": f"Bearer {settings.supabase_service_role_key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def user_headers(access_token: str | None) -> dict[str, str]:
    """사용자 access token으로 Supabase REST API를 호출할 때 사용하는 헤더입니다.

    apikey에는 anon key를 넣고 Authorization에는 사용자 access token을 넣습니다.
    이 방식으로 조회하면 Supabase RLS가 auth.uid()를 기준으로 적용됩니다.
    """

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_anon_key or not access_token:
        raise HTTPException(status_code=500, detail="Supabase anon key 또는 token을 확인하세요.")
    return {
        "apikey": settings.supabase_anon_key,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


def cache_key(user_id: str, message: str) -> str:
    """사용자별/질문별 Redis cache key를 만듭니다.

    user_id를 포함해야 서로 다른 사용자가 같은 질문을 해도 캐시가 섞이지 않습니다.
    """

    return f"ex90:chat:{user_id}:{message}"


def create_mock_answer(message: str) -> AnswerResult:
    """실제 Gemini API를 호출하지 않고 수업용 답변을 만듭니다."""

    return AnswerResult(
        answer=f"'{message}'에 대한 통합 예제용 mock 답변입니다.",
        provider="mock",
        model="mock-integrated-example",
        actual_api_called=False,
    )


def call_gemini(message: str) -> AnswerResult:
    """USE_GEMINI=true일 때 Gemini SDK를 호출합니다."""

    settings = get_settings()
    if not settings.gemini_api_key:
        raise RuntimeError("USE_GEMINI=true이지만 GEMINI_API_KEY가 없습니다.")

    from google import genai

    client = genai.Client(api_key=settings.gemini_api_key)
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=message,
    )
    return AnswerResult(
        answer=response.text or "",
        provider="gemini",
        model=settings.gemini_model,
        actual_api_called=True,
    )


def create_answer(message: str) -> AnswerResult:
    """환경변수 USE_GEMINI 값에 따라 mock 또는 Gemini 답변을 생성합니다."""

    settings = get_settings()
    if settings.use_gemini:
        return call_gemini(message)
    return create_mock_answer(message)


def insert_log(
    user: UserPublic,
    request: ChatRequest,
    answer: str | None,
    cached: bool,
    provider: str,
    model: str,
    actual_api_called: bool,
    status: str = "success",
    error_message: str | None = None,
) -> str | None:
    """채팅 처리 결과를 Supabase 로그 테이블에 저장합니다.

    저장은 service role key로 수행합니다.
    이 예제에서는 FastAPI가 먼저 Bearer token을 검증한 뒤,
    검증된 user.id를 user_id 컬럼에 넣어 저장합니다.
    """

    payload = {
        "user_id": user.id,
        "user_message": request.message,
        "assistant_message": answer,
        "provider": provider,
        "model": model,
        "actual_api_called": actual_api_called,
        "cached": cached,
        "status": status,
        "error_message": error_message,
    }
    try:
        response = httpx.post(table_url(), headers=service_headers(), json=payload, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"로그 저장 실패: {error}") from error
    data = response.json()
    return str(data[0]["id"]) if data else None


def answer_with_cache_and_log(user: UserPublic, request: ChatRequest) -> ChatResponse:
    """캐시 확인, 답변 생성, 로그 저장을 하나의 요청 흐름으로 연결합니다."""

    key = cache_key(user.id, request.message)
    # 1. 먼저 Redis에서 같은 사용자의 같은 질문 답변이 있는지 확인합니다.
    cached_answer = redis_service.get_answer(key)

    if cached_answer:
        # 2. 캐시가 있으면 AI를 다시 호출하지 않고 캐시 답변을 반환합니다.
        #    그래도 "캐시를 사용했다"는 사실은 Supabase 로그에 남깁니다.
        log_id = insert_log(
            user=user,
            request=request,
            answer=cached_answer,
            cached=True,
            provider="redis-cache",
            model="cached-answer",
            actual_api_called=False,
        )
        return ChatResponse(
            user_message=request.message,
            assistant_message=cached_answer,
            cached=True,
            provider="redis-cache",
            model="cached-answer",
            actual_api_called=False,
            log_id=log_id,
        )

    try:
        # 3. 캐시가 없으면 mock 또는 Gemini로 새 답변을 만듭니다.
        answer_result = create_answer(request.message)
    except Exception as error:
        settings = get_settings()
        log_id = insert_log(
            user=user,
            request=request,
            answer=None,
            cached=False,
            provider="gemini" if settings.use_gemini else "mock",
            model=settings.gemini_model if settings.use_gemini else "mock-integrated-example",
            actual_api_called=settings.use_gemini,
            status="error",
            error_message=str(error),
        )
        raise HTTPException(
            status_code=502,
            detail={
                "message": "AI 답변 생성에 실패했습니다.",
                "log_id": log_id,
                "error": str(error),
            },
        ) from error

    # 4. 새로 만든 답변은 다음 요청에서 재사용할 수 있도록 Redis에 저장합니다.
    redis_service.set_answer(key, answer_result.answer)
    # 5. 최종 처리 결과를 Supabase에 저장합니다.
    log_id = insert_log(
        user=user,
        request=request,
        answer=answer_result.answer,
        cached=False,
        provider=answer_result.provider,
        model=answer_result.model,
        actual_api_called=answer_result.actual_api_called,
    )
    return ChatResponse(
        user_message=request.message,
        assistant_message=answer_result.answer,
        cached=False,
        provider=answer_result.provider,
        model=answer_result.model,
        actual_api_called=answer_result.actual_api_called,
        log_id=log_id,
    )


def to_log_public(row: dict) -> ChatLogPublic:
    """Supabase row를 ChatLogPublic 응답 모델로 변환합니다."""

    return ChatLogPublic(
        id=str(row["id"]),
        user_id=str(row["user_id"]),
        user_message=row["user_message"],
        assistant_message=row.get("assistant_message"),
        provider=row["provider"],
        model=row.get("model"),
        actual_api_called=bool(row.get("actual_api_called", False)),
        cached=bool(row["cached"]),
        status=row["status"],
        error_message=row.get("error_message"),
        created_at=row.get("created_at"),
    )


def list_logs(access_token: str | None) -> list[ChatLogPublic]:
    """현재 사용자 token으로 조회 가능한 채팅 로그를 가져옵니다.

    이 조회는 anon key + 사용자 access token으로 수행하므로 RLS가 실제로 적용됩니다.
    """

    try:
        response = httpx.get(
            table_url(),
            headers=user_headers(access_token),
            params={"select": "*", "order": "created_at.desc", "limit": "20"},
            timeout=10,
        )
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"로그 조회 실패: {error}") from error
    return [to_log_public(row) for row in response.json()]
