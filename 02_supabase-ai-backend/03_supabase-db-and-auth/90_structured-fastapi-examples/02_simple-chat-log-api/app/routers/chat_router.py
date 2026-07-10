"""채팅 로그 API 경로를 정의합니다."""

from fastapi import APIRouter

from app.core.config import is_configured
from app.schemas.chat_schema import ChatRequest, ChatResponse, ChatLogPublic
from app.services import chat_service


# 채팅 로그와 관련된 endpoint를 한 router에 모읍니다.
router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    """서버 실행 여부와 Supabase 환경변수 준비 여부를 확인합니다."""

    return {"status": "ok", "supabase_configured": is_configured()}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """사용자 질문을 mock 답변으로 처리하고 Supabase에 로그를 남깁니다."""

    return chat_service.answer_and_log(request)


@router.get("/logs")
def list_logs() -> dict[str, int | list[ChatLogPublic]]:
    """최근 채팅 로그 목록을 조회합니다."""

    logs = chat_service.list_logs()
    return {"count": len(logs), "data": logs}
