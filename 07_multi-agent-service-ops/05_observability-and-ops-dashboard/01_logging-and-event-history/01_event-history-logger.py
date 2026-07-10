r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard\01_logging-and-event-history

Run command:
    python .\01_event-history-logger.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""AI 서비스 운영 이벤트를 구조화해서 기록하는 예제입니다."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from itertools import count


_event_counter = count(start=1)


@dataclass
class EventLog:
    """운영 이벤트 한 건을 표현합니다."""

    event_id: int
    service_name: str
    agent_name: str
    event_type: str
    status: str
    message: str
    created_at: str


def now_iso() -> str:
    """UTC 기준 현재 시간을 ISO 형식 문자열로 반환합니다."""

    return datetime.now(timezone.utc).isoformat()


def create_event(
    service_name: str,
    agent_name: str,
    event_type: str,
    status: str,
    message: str,
) -> EventLog:
    """운영 이벤트를 하나 생성합니다."""

    return EventLog(
        event_id=next(_event_counter),
        service_name=service_name,
        agent_name=agent_name,
        event_type=event_type,
        status=status,
        message=message,
        created_at=now_iso(),
    )


def main() -> None:
    """샘플 이벤트를 생성하고 딕셔너리 형태로 출력합니다."""

    events = [
        create_event("backend", "supervisor_agent", "request_received", "success", "요청 수신"),
        create_event("worker", "ops_agent", "tool_started", "running", "health check 실행"),
        create_event("worker", "ops_agent", "tool_finished", "success", "health check 정상"),
        create_event("monitor", "monitor_agent", "dashboard_refresh", "success", "대시보드 갱신"),
    ]

    for event in events:
        print(asdict(event))


if __name__ == "__main__":
    main()
