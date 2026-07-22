"""Auth 요청/응답 모델입니다."""

from pydantic import BaseModel, Field


class AuthRequest(BaseModel):
    """회원가입과 로그인 요청 Body입니다."""

    email: str = Field(min_length=3, examples=["student@example.com"])
    password: str = Field(min_length=6, examples=["password123"])


class UserPublic(BaseModel):
    """API 응답에서 보여 줄 사용자 정보입니다."""

    id: str
    email: str | None = None
    # access_token은 로그인 직후나 인증 흐름 설명을 위해 포함합니다.
    # 실제 운영 화면에서는 token을 화면에 그대로 오래 노출하지 않습니다.
    access_token: str | None = None


class AuthResponse(BaseModel):
    """로그인 성공 응답입니다."""

    user: UserPublic
    access_token: str
    token_type: str = "bearer"
