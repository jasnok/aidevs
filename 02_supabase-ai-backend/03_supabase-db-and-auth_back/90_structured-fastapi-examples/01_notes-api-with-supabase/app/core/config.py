"""환경변수를 읽는 작은 설정 모듈입니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


# config.py 위치는 app/core/config.py입니다.
# parents[2]는 예제 루트 폴더이므로, 각 예제 폴더의 .env를 읽을 수 있습니다.
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """Supabase 접속에 필요한 설정입니다."""

    supabase_url: str
    supabase_service_role_key: str


def is_real_value(value: str) -> bool:
    """환경변수가 비어 있지 않고 `.env.example`의 예시 값도 아닌지 확인합니다."""

    return bool(value) and not value.startswith(("your-", "https://your-"))


def get_settings() -> Settings:
    """현재 예제 폴더의 `.env` 값을 읽어 Settings로 반환합니다."""

    return Settings(
        # strip()은 앞뒤 공백을 제거합니다.
        # rstrip("/")은 URL 끝의 / 때문에 REST URL이 //처럼 중복되는 일을 줄입니다.
        supabase_url=os.getenv("SUPABASE_URL", "").strip().rstrip("/"),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip(),
    )


def is_configured() -> bool:
    """필수 환경변수가 준비되었는지 확인합니다."""

    settings = get_settings()
    return is_real_value(settings.supabase_url) and is_real_value(settings.supabase_service_role_key)
