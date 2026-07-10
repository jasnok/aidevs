"""Agent 실행 서비스 starter입니다.

구현할 내용:
    1. ScheduleRequest를 받아 LangGraph Agent를 실행합니다.
    2. AgentState에서 최종 응답과 Tool 호출 이력을 꺼냅니다.
    3. ScheduleResponse 형태로 변환합니다.
"""

from app.graph.schedule_graph import run_schedule_agent
from app.schemas.agent_state import ScheduleRequest, ScheduleResponse


def run_agent_service(request: ScheduleRequest) -> ScheduleResponse:
    """API router에서 호출할 서비스 함수입니다."""
    state = run_schedule_agent(request.message)
    return ScheduleResponse(
        answer=state.get("final_answer", ""),
        tools_called=state.get("tools_called", []),
        error_count=state.get("error_count", 0),
    )
