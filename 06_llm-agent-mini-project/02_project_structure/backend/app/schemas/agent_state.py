"""Agent State와 API 모델을 정의하는 파일입니다.

구현할 내용:
    1. 사용자의 일정 요청을 받는 Request 모델을 만듭니다.
    2. Agent가 응답할 Response 모델을 만듭니다.
    3. LangGraph가 공유할 AgentState 타입을 정의합니다.
"""

from typing import TypedDict

from pydantic import BaseModel, Field


class ScheduleRequest(BaseModel):
    """사용자가 일정 조정 Agent에 보내는 요청입니다."""

    message: str = Field(..., min_length=1, examples=["민수, 지영과 내일 30분 회의 잡아줘"])


class ScheduleResponse(BaseModel):
    """Agent 실행 결과를 사용자에게 돌려주는 응답입니다."""

    answer: str
    tools_called: list[str] = Field(default_factory=list)
    error_count: int = 0


class AgentState(TypedDict, total=False):
    """LangGraph Node들이 함께 읽고 수정하는 상태입니다."""

    messages: list[dict]
    user_request: str
    participants: list[str]
    date_range: str
    duration_minutes: int
    required_tools: list[str]
    tools_called: list[str]
    tool_results: dict
    error_count: int
    iteration: int
    reflection_notes: list[str]
    final_answer: str
