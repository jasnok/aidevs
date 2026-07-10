r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\03_multi-tool-orchestration

실행 명령:
    python .\02_manual-tool-selection-flow.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""LLM 없이 조건문으로 도구 선택 흐름을 연습하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class ToolDecision:
    """어떤 도구를 선택했는지 기록하는 데이터 구조입니다."""

    tool_name: str
    reason: str


def select_tool(user_request: str) -> ToolDecision:
    """사용자 요청 문장을 보고 필요한 도구를 단순 규칙으로 선택합니다."""
    lowered = user_request.lower()

    if "총" in user_request or "시간" in user_request:
        return ToolDecision("calculate_total_minutes", "총 학습 시간을 계산해야 하기 때문입니다.")
    if "추천" in user_request or "다음" in user_request:
        return ToolDecision("recommend_next_topic", "다음 학습 주제를 제안해야 하기 때문입니다.")
    if "로그" in user_request or "조회" in user_request:
        return ToolDecision("get_learning_logs", "학습 로그 목록이 필요하기 때문입니다.")
    if "weather" in lowered or "날씨" in user_request:
        return ToolDecision("get_mock_weather", "날씨 정보 조회가 필요하기 때문입니다.")

    return ToolDecision("none", "사용할 도구가 명확하지 않습니다.")


requests = [
    "Kim 학습자의 학습 로그를 조회해줘.",
    "Kim 학습자의 총 학습 시간을 알려줘.",
    "FastAPI 다음에는 무엇을 공부하면 좋을까?",
    "오늘 서울 날씨를 알려줘.",
]

for request in requests:
    decision = select_tool(request)
    print("요청:", request)
    print("선택 도구:", decision.tool_name)
    print("이유:", decision.reason)
    print()
