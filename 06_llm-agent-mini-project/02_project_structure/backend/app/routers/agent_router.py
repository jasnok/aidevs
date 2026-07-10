"""일정 조정 Agent API router starter입니다.

구현할 내용:
    1. POST /agent/schedule endpoint를 만듭니다.
    2. 요청 본문으로 ScheduleRequest를 받습니다.
    3. Agent 실행 결과를 ScheduleResponse로 반환합니다.
"""

from fastapi import APIRouter

from app.schemas.agent_state import ScheduleRequest, ScheduleResponse
from app.services.agent_service import run_agent_service


router = APIRouter()


@router.post("/schedule", response_model=ScheduleResponse)
def schedule_agent(request: ScheduleRequest) -> ScheduleResponse:
    """사용자의 일정 요청을 Agent로 처리합니다."""
    return run_agent_service(request)
