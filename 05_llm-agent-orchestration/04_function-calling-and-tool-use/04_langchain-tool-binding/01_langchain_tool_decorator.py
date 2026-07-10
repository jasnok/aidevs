r"""LangChain @tool 데코레이터로 Python 함수를 Tool 객체로 만드는 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use

실행 명령:
    python .\04_langchain-tool-binding\01_langchain_tool_decorator.py

이 예제는 OpenAI API를 호출하지 않습니다.
일반 Python 함수가 Agent가 사용할 수 있는 Tool 형태로 바뀌는 과정만 확인합니다.
"""

from langchain_core.tools import tool


@tool
def calculate_total_minutes(minutes: list[int]) -> int:
    """학습 시간 목록을 받아 총 학습 시간을 계산합니다."""
    return sum(minutes)


@tool
def recommend_next_topic(current_topic: str) -> str:
    """현재 학습 주제를 보고 다음 학습 주제를 추천합니다."""
    recommendations = {
        "fastapi": "Pydantic 검증과 예외 처리",
        "prompt": "Structured Output과 Prompt Injection 방어",
        "tool": "LangGraph Tool Node",
        "rag": "pgvector 검색과 RAG 품질 평가",
    }
    return recommendations.get(current_topic.lower(), "LangGraph State 흐름")


def main() -> None:
    """Tool 객체의 이름, 설명, 입력 schema를 확인합니다."""
    tools = [calculate_total_minutes, recommend_next_topic]

    for item in tools:
        print("\n--- Tool 정보 ---")
        print("이름:", item.name)
        print("설명:", item.description)
        print("입력 schema:", item.args)

    print("\n--- 직접 실행 결과 ---")
    print(calculate_total_minutes.invoke({"minutes": [30, 45, 20]}))
    print(recommend_next_topic.invoke({"current_topic": "rag"}))


if __name__ == "__main__":
    main()
