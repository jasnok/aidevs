r"""Mini Agent 02의 동일한 TravelPlan Schema 결과를 Provider별로 비교합니다.

실행 전 준비:
    cd C:\mini_agent_st\mini_agent_02_structured_output\backend
    uvicorn app.main:app --reload --port 8000

다른 주소를 사용하면 BACKEND_API_URL 환경 변수로 지정합니다.
"""

import os

import httpx
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")


def compare_providers() -> None:
    response = httpx.post(
        f"{BASE_URL}/api/structured/compare",
        json={
            "providers": ["mock", "gemini", "openai", "ollama"],
            "message": "부산에서 대중교통으로 즐기는 2박 3일 여행을 제안해 주세요.",
        },
        timeout=90,
    )
    response.raise_for_status()

    for item in response.json()["results"]:
        print(f"\n[{item['provider']}] {item['status']}")
        if item["status"] == "success":
            print(f"{item['model']} · {item['latency_ms']}ms")
            print(item["content"])
        else:
            print(item["error"])


if __name__ == "__main__":
    try:
        compare_providers()
    except httpx.HTTPError as error:
        print("Mini Agent 02 Backend 호출 실패:", error)
        print("Backend를 먼저 실행하고 BACKEND_API_URL을 확인하세요.")
