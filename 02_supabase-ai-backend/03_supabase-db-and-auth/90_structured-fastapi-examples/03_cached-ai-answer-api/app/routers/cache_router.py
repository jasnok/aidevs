"""Redis 캐시 API 경로를 정의합니다."""

from fastapi import APIRouter, Query

from app.core.config import is_configured
from app.schemas.cache_schema import CachedAnswerResponse
from app.services import cache_service


# 캐시 관련 endpoint만 모아 둔 router입니다.
router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    """서버와 Redis 환경변수 설정 상태를 확인합니다."""

    return {"status": "ok", "redis_configured": is_configured()}


@router.get("/ai/mock-answer", response_model=CachedAnswerResponse)
def mock_answer(question: str = Query(min_length=1)) -> CachedAnswerResponse:
    """질문에 대한 mock 답변을 Redis에서 찾거나 새로 만들어 저장합니다."""

    return cache_service.get_or_create_answer(question)


@router.delete("/ai/mock-answer-cache")
def clear_cache(question: str = Query(min_length=1)) -> dict[str, str | int]:
    """실습 중 특정 질문의 캐시를 지우고 싶을 때 사용합니다."""

    deleted_count = cache_service.clear_answer(question)
    return {"question": question, "deleted_count": deleted_count}
