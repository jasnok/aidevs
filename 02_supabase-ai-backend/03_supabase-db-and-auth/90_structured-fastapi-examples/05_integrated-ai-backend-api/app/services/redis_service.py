"""Upstash Redis helper입니다."""

from __future__ import annotations

from urllib.parse import quote

import httpx
from fastapi import HTTPException

from app.core.config import get_settings


TTL_SECONDS = 60


def redis_command(*parts: str) -> dict:
    """Upstash Redis REST API로 Redis 명령을 실행합니다.

    예: redis_command("get", "key")는 Redis의 GET key 명령과 같습니다.
    Upstash REST API는 Redis 명령을 URL 경로 형태로 보낼 수 있습니다.
    """

    settings = get_settings()
    if not settings.redis_rest_url or not settings.redis_rest_token:
        raise HTTPException(status_code=500, detail="Upstash Redis 환경변수를 확인하세요.")
    # 질문에는 한글이나 공백이 들어갈 수 있으므로 URL-safe하게 인코딩합니다.
    encoded = [quote(part, safe="") for part in parts]
    url = f"{settings.redis_rest_url}/{'/'.join(encoded)}"
    headers = {"Authorization": f"Bearer {settings.redis_rest_token}"}
    try:
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"Redis 호출 실패: {error}") from error
    return response.json()


def get_answer(key: str) -> str | None:
    """Redis에서 캐시된 답변을 조회합니다."""

    return redis_command("get", key).get("result")


def set_answer(key: str, answer: str) -> None:
    """답변을 Redis에 TTL과 함께 저장합니다.

    ex 옵션은 초 단위 만료 시간입니다.
    현재 예제에서는 60초가 지나면 같은 질문 캐시가 자동으로 사라집니다.
    """

    redis_command("set", key, answer, "ex", str(TTL_SECONDS))
