"""Auth와 상태 확인 API입니다."""

from fastapi import APIRouter

from app.core.config import config_status
from app.schemas.auth_schema import AuthRequest, AuthResponse, UserPublic
from app.services import auth_service


# 통합 예제의 인증 endpoint를 모은 router입니다.
router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | dict[str, bool]]:
    """서버 실행 여부와 Supabase/Redis/Gemini 환경변수 준비 상태를 확인합니다."""

    return {"status": "ok", "configured": config_status()}


@router.post("/auth/signup", response_model=UserPublic)
def signup(request: AuthRequest) -> UserPublic:
    """Supabase Auth 회원가입을 요청합니다."""

    return auth_service.signup(request)


@router.post("/auth/signin", response_model=AuthResponse)
def signin(request: AuthRequest) -> AuthResponse:
    """Supabase Auth 로그인 후 access token을 반환합니다."""

    return auth_service.signin(request)


@router.get("/me", response_model=UserPublic)
def me(user: auth_service.CurrentUser) -> UserPublic:
    """Swagger Authorize에 넣은 token이 가리키는 현재 사용자를 반환합니다."""

    return user
