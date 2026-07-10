r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\02_tool-use-with-external-api

실행 명령:
    python .\02_http-api-tool-wrapper.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""HTTP API 호출을 도구 함수로 감싸는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

MOCK_API_BASE_URL = os.getenv("MOCK_API_BASE_URL", "http://127.0.0.1:8000")


def get_backend_health() -> dict:
    """FastAPI 백엔드의 health API를 호출합니다."""
    try:
        response = httpx.get(f"{MOCK_API_BASE_URL}/health", timeout=5.0)
        response.raise_for_status()
    except httpx.HTTPError as error:
        return {"ok": False, "error": str(error)}
    return {"ok": True, "data": response.json()}


if __name__ == "__main__":
    print(get_backend_health())
