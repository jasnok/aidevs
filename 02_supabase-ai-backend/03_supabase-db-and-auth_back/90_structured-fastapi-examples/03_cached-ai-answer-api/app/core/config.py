"""Upstash Redis 환경변수를 읽습니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


# 이 예제는 Upstash Redis만 사용하므로 Redis 관련 환경변수만 읽습니다.
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """Upstash Redis 접속에 필요한 설정입니다."""

    redis_rest_url: str
    redis_rest_token: str


def is_real_value(value: str) -> bool:
    """환경변수가 비어 있지 않고 `.env.example`의 예시 값도 아닌지 확인합니다."""

    return bool(value) and not value.startswith(("your-", "https://your-"))


def get_settings() -> Settings:
    """현재 예제 폴더의 `.env` 값을 읽어 Settings로 반환합니다."""

    return Settings(
        # Upstash REST URL은 보통 https://... 형태입니다.
        # 끝의 /는 명령 URL을 만들 때 중복되지 않도록 제거합니다.
        redis_rest_url=os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/"),
        redis_rest_token=os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip(),
    )


def is_configured() -> bool:
    """필수 환경변수가 실제 값으로 준비되었는지 확인합니다."""

    settings = get_settings()
    return is_real_value(settings.redis_rest_url) and is_real_value(settings.redis_rest_token)
