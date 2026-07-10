r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\02_conditional-routing

실행 명령:
    python .\02_retry-and-reflection-flow.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""답변을 검토하고 부족하면 한 번 재시도하는 self-reflection 흐름 예제입니다."""

from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class ReflectionState(TypedDict):
    """재시도 흐름에서 사용할 상태입니다."""

    question: str
    answer: str
    feedback: str
    retry_count: int
    approved: bool


def generate_answer(state: ReflectionState) -> dict:
    """retry_count에 따라 처음 답변과 개선 답변을 만듭니다."""
    if state["retry_count"] == 0:
        return {"answer": "FastAPI는 API 도구입니다."}
    return {"answer": "FastAPI는 Python으로 API 서버를 빠르게 만들 수 있는 웹 프레임워크입니다."}


def review_answer(state: ReflectionState) -> dict:
    """답변 길이와 핵심 단어 포함 여부를 기준으로 검토합니다."""
    answer = state["answer"]
    is_good = len(answer) >= 30 and "Python" in answer and "API" in answer
    if is_good:
        return {"approved": True, "feedback": "충분한 답변입니다."}
    return {
        "approved": False,
        "feedback": "답변이 너무 짧거나 핵심 단어가 부족합니다.",
        "retry_count": state["retry_count"] + 1,
    }


def decide_next(state: ReflectionState) -> Literal["generate_answer", "end"]:
    """검토 결과에 따라 재시도 또는 종료를 선택합니다."""
    if state["approved"] or state["retry_count"] >= 1:
        return "end"
    return "generate_answer"


graph_builder = StateGraph(ReflectionState)
graph_builder.add_node("generate_answer", generate_answer)
graph_builder.add_node("review_answer", review_answer)

graph_builder.add_edge(START, "generate_answer")
graph_builder.add_edge("generate_answer", "review_answer")
graph_builder.add_conditional_edges("review_answer", decide_next, {"generate_answer": "generate_answer", "end": END})

graph = graph_builder.compile()

result = graph.invoke(
    {
        "question": "FastAPI가 뭐야?",
        "answer": "",
        "feedback": "",
        "retry_count": 0,
        "approved": False,
    }
)

print(result)
