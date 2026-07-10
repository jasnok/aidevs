r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\01_langgraph-basic-state-node-edge

실행 명령:
    python .\02_multi-step-state-update.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""여러 노드가 상태를 단계적으로 업데이트하는 예제입니다."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class AgentState(TypedDict):
    """여러 노드가 공유하는 상태입니다."""

    user_request: str
    intent: str
    plan: list[str]
    answer: str


def analyze_intent(state: AgentState) -> dict:
    """사용자 요청에서 간단한 의도를 분류합니다."""
    request = state["user_request"]
    if "요약" in request:
        return {"intent": "summarize"}
    return {"intent": "general"}


def make_plan(state: AgentState) -> dict:
    """의도에 따라 작업 계획을 만듭니다."""
    if state["intent"] == "summarize":
        return {"plan": ["로그 조회", "핵심 내용 추출", "요약 생성"]}
    return {"plan": ["요청 확인", "답변 생성"]}


def generate_answer(state: AgentState) -> dict:
    """계획을 바탕으로 최종 답변을 만듭니다."""
    plan_text = " -> ".join(state["plan"])
    return {"answer": f"처리 계획: {plan_text}"}


graph_builder = StateGraph(AgentState)
graph_builder.add_node("analyze_intent", analyze_intent)
graph_builder.add_node("make_plan", make_plan)
graph_builder.add_node("generate_answer", generate_answer)

graph_builder.add_edge(START, "analyze_intent")
graph_builder.add_edge("analyze_intent", "make_plan")
graph_builder.add_edge("make_plan", "generate_answer")
graph_builder.add_edge("generate_answer", END)

graph = graph_builder.compile()

result = graph.invoke(
    {
        "user_request": "이번 주 학습 로그를 요약해줘",
        "intent": "",
        "plan": [],
        "answer": "",
    }
)

print(result)
