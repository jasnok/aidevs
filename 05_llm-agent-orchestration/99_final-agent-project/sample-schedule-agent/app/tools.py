r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent\app

실행 명령:
    python .\tools.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""일정 조정 에이전트가 사용하는 도구 함수입니다."""

from app.mock_data import SCHEDULES


def extract_participants(user_request: str) -> list[str]:
    """사용자 요청에서 참석자 이름을 추출합니다."""
    participants = [name for name in SCHEDULES if name.lower() in user_request.lower()]
    if participants:
        return participants
    return list(SCHEDULES.keys())


def find_common_available_slots(participants: list[str]) -> list[str]:
    """참석자들이 모두 가능한 시간대를 찾습니다."""
    if not participants:
        return []

    available = set(SCHEDULES.get(participants[0], []))
    for participant in participants[1:]:
        available &= set(SCHEDULES.get(participant, []))

    return sorted(available)


def select_best_slot(available_slots: list[str]) -> str:
    """가능한 시간대 중 첫 번째 후보를 선택합니다."""
    if not available_slots:
        return ""
    return available_slots[0]


def build_rule_based_message(participants: list[str], selected_slot: str, duration_minutes: int) -> str:
    """LLM 없이 사용할 수 있는 규칙 기반 일정 제안 메시지를 만듭니다."""
    if not selected_slot:
        return "공통으로 가능한 시간대를 찾지 못했습니다. 다른 후보 시간을 확인해 주세요."

    names = ", ".join(participants)
    return f"{names} 참석자 기준으로 {selected_slot}에 {duration_minutes}분 회의를 제안합니다."
