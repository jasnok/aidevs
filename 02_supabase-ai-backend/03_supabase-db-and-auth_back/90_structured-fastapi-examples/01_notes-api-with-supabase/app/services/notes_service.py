"""Supabase `ex90_notes` 테이블을 호출하는 service 모듈입니다."""

from __future__ import annotations

from fastapi import HTTPException, status
from postgrest.exceptions import APIError

from app.core.config import get_settings
from app.schemas.note_schema import NoteCreate, NotePublic, NoteUpdate


TABLE_NAME = "ex90_notes"


def raise_supabase_error(error: APIError) -> None:
    """Supabase/PostgREST 오류를 수강생이 이해하기 쉬운 HTTP 오류로 바꿉니다."""

    error_info = error.args[0] if error.args and isinstance(error.args[0], dict) else {}
    code = error_info.get("code")
    message = error_info.get("message", str(error))

    if code == "PGRST205" and TABLE_NAME in message:
        detail = (
            f"Supabase에서 '{TABLE_NAME}' 테이블을 찾을 수 없습니다. "
            "이 예제 폴더의 schema.sql을 Supabase SQL Editor에서 먼저 실행하세요."
        )
    else:
        detail = f"Supabase 요청에 실패했습니다. 원인: {message}"

    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail=detail,
    ) from error


def execute_query(query):
    """Supabase query 실행 중 발생한 APIError를 읽기 쉬운 오류로 변환합니다."""

    try:
        return query.execute()
    except APIError as error:
        raise_supabase_error(error)


def get_supabase_client():
    """Supabase client를 만듭니다. 외부 패키지 import는 실제 호출 시점에 합니다."""

    # supabase 패키지는 이 함수가 호출될 때 import합니다.
    # 이렇게 하면 테스트나 OpenAPI 확인처럼 DB를 쓰지 않는 작업에서 import 부담이 줄어듭니다.
    from supabase import create_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=".env의 SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY를 확인하세요.",
        )

    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def to_note_public(row: dict) -> NotePublic:
    """Supabase row를 응답 모델로 변환합니다."""

    return NotePublic(
        id=str(row["id"]),
        title=row["title"],
        content=row["content"],
        created_at=row.get("created_at"),
    )


def list_notes() -> list[NotePublic]:
    """최근 노트를 조회합니다."""

    # Supabase Python client의 기본 흐름입니다.
    # table -> select/order/limit 같은 조건 구성 -> execute로 실제 요청 전송
    query = (
        get_supabase_client()
        .table(TABLE_NAME)
        .select("*")
        .order("created_at", desc=True)
        .limit(20)
    )
    result = execute_query(query)
    return [to_note_public(row) for row in result.data]


def create_note(note: NoteCreate) -> NotePublic:
    """새 노트를 저장합니다."""

    # Pydantic 모델을 그대로 넘기지 않고 필요한 컬럼만 딕셔너리로 구성합니다.
    # 이렇게 하면 DB에 저장할 필드를 코드에서 명확히 볼 수 있습니다.
    query = (
        get_supabase_client()
        .table(TABLE_NAME)
        .insert({"title": note.title, "content": note.content})
    )
    result = execute_query(query)
    return to_note_public(result.data[0])


def get_note(note_id: str) -> NotePublic | None:
    """id로 노트 1개를 조회합니다."""

    # eq("id", note_id)는 SQL의 WHERE id = ... 조건과 비슷합니다.
    # limit(1)은 결과를 최대 1개만 가져오겠다는 뜻입니다.
    query = (
        get_supabase_client()
        .table(TABLE_NAME)
        .select("*")
        .eq("id", note_id)
        .limit(1)
    )
    result = execute_query(query)
    if not result.data:
        return None
    return to_note_public(result.data[0])


def update_note(note_id: str, note: NoteUpdate) -> NotePublic | None:
    """id 조건으로 노트를 수정합니다."""

    # update 뒤에 eq 조건을 붙여야 특정 노트 1개만 수정합니다.
    # 조건 없이 update/delete를 실행하는 습관은 실제 서비스에서 매우 위험합니다.
    query = (
        get_supabase_client()
        .table(TABLE_NAME)
        .update({"title": note.title, "content": note.content})
        .eq("id", note_id)
    )
    result = execute_query(query)
    if not result.data:
        return None
    return to_note_public(result.data[0])


def delete_note(note_id: str) -> bool:
    """id 조건으로 노트를 삭제합니다."""

    # 삭제도 반드시 eq 조건으로 대상을 제한합니다.
    query = get_supabase_client().table(TABLE_NAME).delete().eq("id", note_id)
    result = execute_query(query)
    return bool(result.data)
