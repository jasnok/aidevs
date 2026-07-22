"""Supabase Auth와 Bearer token 확인을 담당합니다."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Header, status

from app.core.config import get_settings
from app.schemas.auth_schema import AuthRequest, AuthResponse, UserPublic


def get_supabase_client():
    """Supabase Auth API를 호출할 client를 만듭니다."""

    from supabase import create_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(status_code=500, detail="Supabase 환경변수를 확인하세요.")
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def signup(request: AuthRequest) -> UserPublic:
    """이메일/비밀번호로 Supabase Auth 회원가입을 요청합니다."""

    try:
        # 사용자 계정 생성은 FastAPI가 직접 DB에 insert하지 않습니다.
        # Supabase Auth가 auth.users 테이블과 인증 절차를 관리합니다.
        response = get_supabase_client().auth.sign_up(
            {"email": request.email, "password": request.password}
        )
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"sign up 실패: {error}") from error

    if response.user is None:
        raise HTTPException(status_code=400, detail="user가 없는 signup 응답입니다.")
    return UserPublic(id=response.user.id, email=response.user.email)


def signin(request: AuthRequest) -> AuthResponse:
    """이메일/비밀번호로 로그인하고 Supabase access token을 받습니다."""

    try:
        # 로그인에 성공하면 Supabase가 session과 access_token을 반환합니다.
        # 이 token은 이후 Authorization: Bearer <token> 헤더로 사용합니다.
        response = get_supabase_client().auth.sign_in_with_password(
            {"email": request.email, "password": request.password}
        )
    except Exception as error:
        raise HTTPException(status_code=401, detail=f"sign in 실패: {error}") from error

    if response.user is None or response.session is None:
        raise HTTPException(status_code=401, detail="로그인 응답에 user/session이 없습니다.")

    user = UserPublic(
        id=response.user.id,
        email=response.user.email,
        access_token=response.session.access_token,
    )
    return AuthResponse(user=user, access_token=response.session.access_token)


def get_current_user(authorization: str | None = Header(default=None)) -> UserPublic:
    """Authorization 헤더의 Bearer token으로 현재 사용자를 확인합니다.

    이 예제는 Header를 직접 읽는 기본 방식을 보여 줍니다.
    Swagger에서 token을 한 번만 저장하고 싶다면 05 통합 예제처럼 HTTPBearer를 사용합니다.
    """

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization: Bearer <access_token> 헤더가 필요합니다.",
        )

    # "Bearer abc.def.ghi"에서 실제 token 부분만 꺼냅니다.
    token = authorization.removeprefix("Bearer ").strip()
    try:
        # token 검증은 Supabase Auth에 맡깁니다.
        # 유효한 token이면 response.user에 현재 사용자 정보가 들어옵니다.
        response = get_supabase_client().auth.get_user(token)
    except Exception as error:
        raise HTTPException(status_code=401, detail=f"token 확인 실패: {error}") from error

    if response.user is None:
        raise HTTPException(status_code=401, detail="유효하지 않은 token입니다.")
    return UserPublic(id=response.user.id, email=response.user.email, access_token=token)


CurrentUser = Annotated[UserPublic, Depends(get_current_user)]
