r"""Mini Agent Backend에서 Provider별 Tool 선택과 안전 실행을 확인합니다.

실행 전 준비:
    cd C:\mini_agent_st\mini_agent_03_tool\backend
    uvicorn app.main:app --reload --port 8000

다른 주소를 사용하면 BACKEND_API_URL 환경 변수로 지정합니다.
"""

import os

import httpx


BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000").rstrip("/")
QUESTION = "부산 날씨를 알려줘"


def post(path: str, payload: dict) -> dict:
    response = httpx.post(f"{BACKEND_API_URL}{path}", json=payload, timeout=60)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    comparison = post(
        "/api/tools/compare",
        {"providers": ["mock", "gemini", "openai", "ollama"], "message": QUESTION},
    )
    print("1. Provider별 Tool 선택")
    for item in comparison["results"]:
        print(item)

    decision = post("/api/tools/select", {"provider": "mock", "message": QUESTION})
    print("\n2. Mock Tool Call", decision)

    if decision["tool_name"]:
        result = post(
            "/api/tools/run",
            {"tool_name": decision["tool_name"], "arguments": decision["arguments"]},
        )
        print("\n3. Backend 검증과 Tool Result", result)
