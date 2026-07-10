r"""Redis에 최근 대화를 캐시하는 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search

실행 명령:
    python .\05_conversation-memory\04_redis-session-cache.py

필요한 준비:
    1. aidev-redis 컨테이너가 실행 중이어야 합니다.
    2. pip install redis python-dotenv
    3. .env 파일에 REDIS_URL이 있으면 그 값을 사용합니다.

이 예제의 목적:
    PostgreSQL은 대화 이력을 안정적으로 저장하는 곳이고,
    Redis는 최근 대화처럼 자주 읽는 데이터를 빠르게 보관하는 곳이라는 차이를 이해합니다.
"""

from pathlib import Path
import json
import os

from dotenv import load_dotenv
import redis


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
SESSION_ID = "demo-session-001"
CACHE_KEY = f"session:{SESSION_ID}:recent_messages"


def main() -> None:
    client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

    print("Redis Session Cache 예제")
    print("redis url:", REDIS_URL)
    print("cache key:", CACHE_KEY)

    # ping은 Redis 서버가 응답하는지 확인하는 가장 작은 테스트입니다.
    client.ping()
    print("Redis 연결 확인: PONG")

    sample_messages = [
        {"role": "user", "content": "LangGraph가 뭐야?"},
        {"role": "assistant", "content": "State, Node, Edge로 Agent 흐름을 관리하는 도구입니다."},
        {"role": "user", "content": "RAG와 같이 쓸 수 있어?"},
    ]

    # set은 하나의 key에 문자열 값을 저장합니다.
    # JSON으로 바꾸어 저장하면 list/dict 구조도 Redis에 넣을 수 있습니다.
    client.set(CACHE_KEY, json.dumps(sample_messages, ensure_ascii=False), ex=600)
    print("최근 대화 캐시 저장 완료")

    cached_text = client.get(CACHE_KEY)
    if cached_text is None:
        print("캐시가 비어 있습니다.")
        return

    cached_messages = json.loads(cached_text)
    print("\nRedis에서 읽은 최근 대화:")
    for message in cached_messages:
        print(f"- {message['role']}: {message['content']}")

    ttl = client.ttl(CACHE_KEY)
    print(f"\n캐시 만료까지 남은 시간: {ttl}초")


if __name__ == "__main__":
    main()
