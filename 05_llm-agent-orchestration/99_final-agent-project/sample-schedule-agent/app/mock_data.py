r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent\app

실행 명령:
    python .\mock_data.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""실제 캘린더 API 대신 사용하는 Mock 일정 데이터입니다."""

SCHEDULES = {
    "Kim": ["2026-06-08 10:00", "2026-06-08 14:00", "2026-06-09 11:00"],
    "Lee": ["2026-06-08 10:00", "2026-06-08 15:00", "2026-06-09 11:00"],
    "Park": ["2026-06-08 10:00", "2026-06-09 11:00", "2026-06-09 16:00"],
}

DEFAULT_PARTICIPANTS = ["Kim", "Lee", "Park"]
