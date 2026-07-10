r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\03_tool-and-rag-node-flow

실행 명령:
    python .\01_tool-node-style-flow.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""도구 선택과 실행을 LangGraph 노드로 나누는 예제입니다."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class ToolFlowState(TypedDict):
    """도구 실행 흐름에서 사용할 상태입니다."""

    user_request: str
    tool_name: str
    tool_args: dict
    tool_result: str
    final_answer: str


def select_tool(state: ToolFlowState) -> dict:
    """사용자 요청에 따라 사용할 도구를 선택합니다."""
    if "총" in state["user_request"] or "시간" in state["user_request"]:
        return {"tool_name": "calculate_total_minutes", "tool_args": {"minutes": [40, 60, 30]}}
    return {"tool_name": "none", "tool_args": {}}


def execute_tool(state: ToolFlowState) -> dict:
    """선택된 도구를 실행합니다."""
    if state["tool_name"] == "calculate_total_minutes":
        total = sum(state["tool_args"].get("minutes", []))
        return {"tool_result": f"총 학습 시간은 {total}분입니다."}
    return {"tool_result": "실행할 도구가 없습니다."}


def generate_final_answer(state: ToolFlowState) -> dict:
    """도구 실행 결과를 사용자 답변으로 정리합니다."""
    return {"final_answer": state["tool_result"]}


graph_builder = StateGraph(ToolFlowState)
graph_builder.add_node("select_tool", select_tool)
graph_builder.add_node("execute_tool", execute_tool)
graph_builder.add_node("generate_final_answer", generate_final_answer)

graph_builder.add_edge(START, "select_tool")
graph_builder.add_edge("select_tool", "execute_tool")
graph_builder.add_edge("execute_tool", "generate_final_answer")
graph_builder.add_edge("generate_final_answer", END)

graph = graph_builder.compile()

result = graph.invoke(
    {
        "user_request": "이번 주 총 학습 시간을 계산해줘.",
        "tool_name": "",
        "tool_args": {},
        "tool_result": "",
        "final_answer": "",
    }
)

print(result["final_answer"])
