r"""
Upstash Redis에 값을 저장하고, 조회하고, TTL을 확인하는 가장 작은 예제입니다.

실행 위치:
    C:\aidev\02_supabase-ai-backend

실행 명령:
    python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\01_redis_set_get_ttl.py

실행 전 준비:
    1. C:\aidev\02_supabase-ai-backend\.env 파일에 아래 값이 있어야 합니다.

       UPSTASH_REDIS_REST_URL=https://...
       UPSTASH_REDIS_REST_TOKEN=...

    2. Upstash Redis는 설치형 Redis가 아니라, 인터넷으로 호출하는 Redis입니다.
       그래서 이 예제는 Upstash REST API 주소와 token을 사용합니다.
"""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote

import httpx
from dotenv import load_dotenv


# 이 파일은 03_supabase-db-and-auth/06_upstash-redis-cache-and-session 안에 있습니다.
# parents[2]는 C:\aidev\02_supabase-ai-backend 폴더를 의미합니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def get_upstash_env() -> tuple[str, str]:
    """`.env`에서 Upstash Redis 접속 정보를 읽고, 예시 값이면 오류를 냅니다."""

    load_dotenv(ENV_PATH)

    rest_url = os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/")
    rest_token = os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip()

    if not rest_url or not rest_token:
        raise RuntimeError(
            "Upstash Redis 환경변수가 준비되지 않았습니다. "
            "C:\\aidev\\02_supabase-ai-backend\\.env 파일의 "
            "UPSTASH_REDIS_REST_URL, UPSTASH_REDIS_REST_TOKEN 값을 확인하세요."
        )

    if rest_url.startswith(("your-", "https://your-")) or rest_token.startswith(("your-", "https://your-")):
        raise RuntimeError("Upstash Redis 환경변수에 예시 값이 들어 있습니다. Upstash Console에서 실제 값을 복사해 넣어 주세요.")

    return rest_url, rest_token


def redis_command(*parts: str) -> dict:
    """
    Upstash Redis REST API로 Redis 명령을 실행합니다.

    예를 들어 redis_command("get", "hello")는 Redis의 GET hello 명령과 같습니다.
    예제를 단순하게 보기 위해 GET 방식의 REST command URL을 사용합니다.
    """

    rest_url, rest_token = get_upstash_env()

    # key나 value에 공백, 한글, 특수문자가 들어가도 URL이 깨지지 않도록 인코딩합니다.
    encoded_parts = [quote(part, safe="") for part in parts]
    command_url = f"{rest_url}/{'/'.join(encoded_parts)}"
    headers = {"Authorization": f"Bearer {rest_token}"}

    response = httpx.get(command_url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """SET, GET, TTL을 순서대로 실행합니다."""

    # Redis는 데이터를 key/value 형태로 저장합니다.
    # key는 데이터를 찾기 위한 이름이고, value는 실제 저장할 값입니다.
    cache_key = "aidev:06:greeting"
    cache_value = "hello upstash redis"

    # TTL은 Time To Live의 줄임말입니다.
    # 아래 값은 이 key를 30초 뒤 자동 삭제하겠다는 뜻입니다.
    ttl_seconds = "30"

    try:
        print("[1] Redis에 값 저장하기")
        print(redis_command("set", cache_key, cache_value, "ex", ttl_seconds))

        print("\n[2] Redis에서 값 조회하기")
        print(redis_command("get", cache_key))

        print("\n[3] 남은 TTL 확인하기")
        print(redis_command("ttl", cache_key))

        print("\n정리: 30초가 지나면 이 key는 Redis에서 자동으로 사라집니다.")
    except (RuntimeError, httpx.HTTPError) as error:
        print("[Upstash Redis 실행 오류]")
        print(error)
        print("\n확인할 것:")
        print("- .env 파일에 UPSTASH_REDIS_REST_URL 값이 있는가?")
        print("- .env 파일에 UPSTASH_REDIS_REST_TOKEN 값이 있는가?")
        print("- Upstash Redis database가 활성 상태인가?")


if __name__ == "__main__":
    main()
