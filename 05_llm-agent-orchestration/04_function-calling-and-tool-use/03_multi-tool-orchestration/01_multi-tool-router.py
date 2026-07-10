r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\03_multi-tool-orchestration

실행 명령:
    python .\01_multi-tool-router.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""여러 도구 이름을 받아 실제 함수로 연결하는 라우터 예제입니다."""

import json


LEARNING_LOGS = [
    {"learner": "Kim", "topic": "FastAPI", "minutes": 80},
    {"learner": "Kim", "topic": "Streamlit", "minutes": 40},
    {"learner": "Lee", "topic": "Docker", "minutes": 60},
]


def get_learning_logs(learner: str) -> list[dict]:
    """학습자 이름으로 학습 로그를 조회합니다."""
    return [log for log in LEARNING_LOGS if log["learner"].lower() == learner.lower()]


def calculate_total_minutes(learner: str) -> int:
    """학습자의 총 학습 시간을 계산합니다."""
    return sum(log["minutes"] for log in get_learning_logs(learner))


def recommend_next_topic(current_topic: str) -> str:
    """현재 주제에 따라 다음 학습 주제를 추천합니다."""
    recommendations = {
        "fastapi": "API 문서화와 예외 처리",
        "streamlit": "Session State와 API 연동",
        "docker": "Docker run과 포트 매핑",
    }
    return recommendations.get(current_topic.lower(), "프로젝트 README 정리")


def call_tool(name: str, arguments: dict) -> str:
    """도구 이름과 인자를 받아 실제 함수를 실행합니다."""
    if name == "get_learning_logs":
        return json.dumps({"logs": get_learning_logs(arguments["learner"])}, ensure_ascii=False)
    if name == "calculate_total_minutes":
        return json.dumps({"minutes": calculate_total_minutes(arguments["learner"])}, ensure_ascii=False)
    if name == "recommend_next_topic":
        return json.dumps({"next_topic": recommend_next_topic(arguments["current_topic"])}, ensure_ascii=False)
    return json.dumps({"error": f"Unknown tool: {name}"}, ensure_ascii=False)


examples = [
    ("get_learning_logs", {"learner": "Kim"}),
    ("calculate_total_minutes", {"learner": "Kim"}),
    ("recommend_next_topic", {"current_topic": "FastAPI"}),
]

for tool_name, tool_args in examples:
    print(tool_name, "->", call_tool(tool_name, tool_args))
