"""일정 조정 Agent가 사용할 Tool 함수 starter입니다.

구현할 내용:
    1. Mock 일정 데이터를 준비합니다.
    2. 참석자별 일정을 조회하는 Tool을 만듭니다.
    3. 가능한 시간 후보를 찾는 Tool을 만듭니다.
    4. 최종 초대 메시지를 만드는 Tool을 만듭니다.

처음에는 실제 Calendar API 대신 Mock data로 구현합니다.
"""


def check_calendar_tool(participants: list[str], date_range: str) -> dict:
    """참석자별 일정을 조회하는 Tool입니다."""
    # TODO: Mock data에서 participants와 date_range에 해당하는 일정을 찾아 반환합니다.
    return {"participants": participants, "date_range": date_range, "busy_slots": []}


def find_available_slot_tool(schedules: dict, duration_minutes: int) -> list[str]:
    """가능한 회의 시간 후보를 찾는 Tool입니다."""
    # TODO: busy_slots를 기준으로 가능한 시간 후보를 계산합니다.
    return []


def draft_invitation_tool(selected_slot: str, participants: list[str]) -> str:
    """선택된 시간과 참석자를 바탕으로 초대 메시지를 만듭니다."""
    # TODO: 사용자에게 보여줄 자연스러운 일정 제안 문장을 만듭니다.
    return f"{selected_slot}에 {', '.join(participants)} 회의를 제안합니다."
