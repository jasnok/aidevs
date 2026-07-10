r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard\04_execution-status-management

Run command:
    python .\01_execution-status-manager.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 실행 상태를 관리하는 예제입니다."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from uuid import uuid4


ExecutionStatus = Literal["pending", "running", "success", "failed", "cancelled"]


@dataclass
class ExecutionRecord:
    """Agent 실행 한 건의 상태를 저장합니다."""

    execution_id: str
    request: str
    status: ExecutionStatus
    current_step: str
    history: list[str] = field(default_factory=list)

    def update(self, status: ExecutionStatus, current_step: str) -> None:
        """실행 상태를 갱신하고 이력을 남깁니다."""

        self.status = status
        self.current_step = current_step
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append(f"{timestamp} | {status} | {current_step}")


def create_execution(request: str) -> ExecutionRecord:
    """새 실행 기록을 생성합니다."""

    record = ExecutionRecord(
        execution_id=str(uuid4()),
        request=request,
        status="pending",
        current_step="created",
    )
    record.update("pending", "created")
    return record


def main() -> None:
    """실행 상태가 단계별로 바뀌는 흐름을 확인합니다."""

    record = create_execution("backend 상태를 점검하고 필요하면 복구해줘")
    record.update("running", "supervisor routing")
    record.update("running", "health check")
    record.update("running", "review result")
    record.update("success", "completed")

    print(record)
    print("\nHistory")
    for item in record.history:
        print(f"- {item}")


if __name__ == "__main__":
    main()
