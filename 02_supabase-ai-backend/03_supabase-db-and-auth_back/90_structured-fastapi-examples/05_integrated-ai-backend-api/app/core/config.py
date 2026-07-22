"""통합 예제의 환경변수 설정입니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


# 통합 예제는 Supabase, Redis, Gemini 설정을 모두 사용합니다.
# 설정이 많아지므로 dataclass Settings로 한 번에 묶어 관리합니다.
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """통합 예제에서 사용하는 외부 서비스 설정입니다."""

    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str
    redis_rest_url: str
    redis_rest_token: str
    use_gemini: bool
    gemini_api_key: str
    gemini_model: str


def parse_bool(value: str | None) -> bool:
    """환경변수 문자열을 bool 값으로 변환합니다."""

    return (value or "").strip().lower() in {"1", "true", "yes", "y"}


def is_real_value(value: str) -> bool:
    """환경변수가 비어 있지 않고 `.env.example`의 예시 값도 아닌지 확인합니다."""

    return bool(value) and not value.startswith(("your-", "https://your-"))


def get_settings() -> Settings:
    """현재 예제 폴더의 `.env` 값을 읽어 Settings로 반환합니다."""

    return Settings(
        # Supabase 관련 설정입니다.
        supabase_url=os.getenv("SUPABASE_URL", "").strip().rstrip("/"),
        supabase_anon_key=os.getenv("SUPABASE_ANON_KEY", "").strip(),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip(),
        # Upstash Redis REST API 설정입니다.
        redis_rest_url=os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/"),
        redis_rest_token=os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip(),
        # USE_GEMINI=true일 때만 실제 Gemini SDK를 호출합니다.
        use_gemini=parse_bool(os.getenv("USE_GEMINI")),
        gemini_api_key=os.getenv("GEMINI_API_KEY", "").strip(),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite").strip(),
    )


def config_status() -> dict[str, bool]:
    """health check에서 보여 줄 환경변수 준비 상태를 반환합니다."""

    settings = get_settings()
    return {
        "supabase_url": is_real_value(settings.supabase_url),
        "supabase_anon_key": is_real_value(settings.supabase_anon_key),
        "supabase_service_role_key": is_real_value(settings.supabase_service_role_key),
        "redis_rest_url": is_real_value(settings.redis_rest_url),
        "redis_rest_token": is_real_value(settings.redis_rest_token),
        "use_gemini": settings.use_gemini,
        "gemini_api_key": is_real_value(settings.gemini_api_key),
    }
