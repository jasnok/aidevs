"""LangGraph 기반 일정 조정 Agent starter입니다.

구현할 내용:
    1. AgentState를 사용하는 StateGraph를 만듭니다.
    2. analyze_request, decide_tool, call_tool, review_result, self_reflect, generate_answer 노드를 구현합니다.
    3. 오류가 있으면 self_reflect 또는 fallback으로 이동하는 조건 분기를 추가합니다.
"""

from app.schemas.agent_state import AgentState


def analyze_request(state: AgentState) -> AgentState:
    """사용자 요청에서 참석자, 날짜, 회의 길이 같은 정보를 추출합니다."""
    # TODO: 규칙 기반 또는 LLM 기반으로 요청을 분석합니다.
    return state


def decide_tool(state: AgentState) -> AgentState:
    """현재 State를 보고 필요한 Tool을 결정합니다."""
    # TODO: 일정 조회, 가능 시간 탐색, 메시지 작성 중 어떤 Tool이 필요한지 결정합니다.
    return state


def call_tool(state: AgentState) -> AgentState:
    """선택된 Tool을 실행하고 결과를 State에 저장합니다."""
    # TODO: app.tools.schedule_tools의 함수를 호출합니다.
    return state


def review_result(state: AgentState) -> AgentState:
    """Tool 결과가 충분하고 일관적인지 검증합니다."""
    # TODO: Tool 결과가 비었거나 최종 응답과 충돌하는지 확인합니다.
    return state


def run_schedule_agent(message: str) -> AgentState:
    """API 또는 UI에서 호출할 Agent 실행 함수입니다."""
    # TODO: StateGraph를 구성하고 invoke합니다.
    # 예: graph = build_graph(); return graph.invoke(initial_state)
    return {
        "user_request": message,
        "tools_called": [],
        "error_count": 0,
        "final_answer": "TODO: LangGraph Agent를 구현하세요.",
    }
