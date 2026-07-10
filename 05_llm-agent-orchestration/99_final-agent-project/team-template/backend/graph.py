r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\team-template\backend

실행 명령:
    python .\graph.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""팀 프로젝트 LangGraph 구현 시작 파일입니다."""

from langgraph.graph import END, START, StateGraph

from agent_state import AgentState
from tools import example_lookup_tool


def analyze_request(state: AgentState) -> dict:
    """사용자 요청을 분석하고 route를 결정합니다."""
    if "검색" in state["user_request"]:
        return {"route": "search"}
    return {"route": "general"}


def execute_tool(state: AgentState) -> dict:
    """route에 따라 도구를 실행합니다."""
    if state["route"] == "search":
        return {"tool_result": example_lookup_tool(state["user_request"])}
    return {"tool_result": "도구 실행이 필요하지 않습니다."}


def generate_answer(state: AgentState) -> dict:
    """최종 답변을 생성합니다."""
    return {"final_answer": f"처리 결과: {state['tool_result']}"}


def build_graph():
    """팀 프로젝트 그래프를 생성합니다."""
    builder = StateGraph(AgentState)
    builder.add_node("analyze_request", analyze_request)
    builder.add_node("execute_tool", execute_tool)
    builder.add_node("generate_answer", generate_answer)
    builder.add_edge(START, "analyze_request")
    builder.add_edge("analyze_request", "execute_tool")
    builder.add_edge("execute_tool", "generate_answer")
    builder.add_edge("generate_answer", END)
    return builder.compile()


def run_agent(user_request: str) -> AgentState:
    """에이전트를 실행합니다."""
    graph = build_graph()
    initial_state: AgentState = {
        "user_request": user_request,
        "route": "",
        "tool_result": "",
        "retrieved_context": [],
        "final_answer": "",
    }
    return graph.invoke(initial_state)


if __name__ == "__main__":
    print(run_agent("수업 자료를 검색해줘")["final_answer"])
