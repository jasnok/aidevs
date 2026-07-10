r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\02_conditional-routing

실행 명령:
    python .\01_conditional-route-basic.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""조건 분기로 다음 노드를 선택하는 LangGraph 예제입니다."""

from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class RouteState(TypedDict):
    """라우팅 예제에서 사용할 상태입니다."""

    user_request: str
    route: str
    result: str


def classify_request(state: RouteState) -> dict:
    """사용자 요청을 보고 어떤 경로로 보낼지 결정합니다."""
    request = state["user_request"]
    if "검색" in request or "자료" in request:
        return {"route": "rag"}
    if "계산" in request or "시간" in request:
        return {"route": "tool"}
    return {"route": "answer"}


def route_next(state: RouteState) -> Literal["rag_node", "tool_node", "answer_node"]:
    """route 값에 따라 다음 노드 이름을 반환합니다."""
    if state["route"] == "rag":
        return "rag_node"
    if state["route"] == "tool":
        return "tool_node"
    return "answer_node"


def rag_node(state: RouteState) -> dict:
    """검색이 필요한 요청을 처리하는 가상 노드입니다."""
    return {"result": "RAG 검색 노드로 이동했습니다."}


def tool_node(state: RouteState) -> dict:
    """도구 실행이 필요한 요청을 처리하는 가상 노드입니다."""
    return {"result": "Tool 실행 노드로 이동했습니다."}


def answer_node(state: RouteState) -> dict:
    """바로 답변 가능한 요청을 처리하는 노드입니다."""
    return {"result": "일반 답변 노드로 이동했습니다."}


graph_builder = StateGraph(RouteState)
graph_builder.add_node("classify_request", classify_request)
graph_builder.add_node("rag_node", rag_node)
graph_builder.add_node("tool_node", tool_node)
graph_builder.add_node("answer_node", answer_node)

graph_builder.add_edge(START, "classify_request")
graph_builder.add_conditional_edges("classify_request", route_next)
graph_builder.add_edge("rag_node", END)
graph_builder.add_edge("tool_node", END)
graph_builder.add_edge("answer_node", END)

graph = graph_builder.compile()

examples = [
    "수업 자료를 검색해줘",
    "총 학습 시간을 계산해줘",
    "FastAPI가 뭐야?",
]

for request in examples:
    result = graph.invoke({"user_request": request, "route": "", "result": ""})
    print(request, "->", result["result"])
