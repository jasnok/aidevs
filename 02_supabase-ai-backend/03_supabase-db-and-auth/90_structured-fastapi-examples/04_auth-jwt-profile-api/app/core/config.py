"""Supabase Auth 예제 설정입니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


# Auth/RLS 예제는 anon key와 service role key를 모두 비교해 봅니다.
# .env는 이 예제 폴더 바로 아래에 둡니다.
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """Supabase Auth와 profile 저장에 필요한 설정입니다."""

    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str


def is_real_value(value: str) -> bool:
    """환경변수가 비어 있지 않고 `.env.example`의 예시 값도 아닌지 확인합니다."""

    return bool(value) and not value.startswith(("your-", "https://your-"))


def get_settings() -> Settings:
    """현재 예제 폴더의 `.env` 값을 읽어 Settings로 반환합니다."""

    return Settings(
        # anon key는 사용자 JWT/RLS 흐름에 사용하고,
        # service role key는 서버 전용 관리자 권한이 필요한 흐름에 사용합니다.
        supabase_url=os.getenv("SUPABASE_URL", "").strip().rstrip("/"),
        supabase_anon_key=os.getenv("SUPABASE_ANON_KEY", "").strip(),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip(),
    )


def is_configured() -> bool:
    """필수 환경변수가 실제 값으로 준비되었는지 확인합니다."""

    settings = get_settings()
    return bool(
        is_real_value(settings.supabase_url)
        and is_real_value(settings.supabase_anon_key)
        and is_real_value(settings.supabase_service_role_key)
    )
