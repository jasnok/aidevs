r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow\02_health-check-retry-restart

Run command:
    python .\01_health-check-retry-restart.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Health Check, Retry, Restart 의사결정을 연습하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class ServiceStatus:
    """서비스 상태를 표현합니다."""

    service_name: str
    is_healthy: bool
    failed_checks: int


def check_health(status: ServiceStatus) -> bool:
    """서비스가 정상인지 Health Check 결과를 반환합니다."""

    return status.is_healthy


def decide_recovery_action(status: ServiceStatus) -> str:
    """실패 횟수에 따라 retry/restart/escalate 중 하나를 선택합니다."""

    if check_health(status):
        return "no_action: 서비스가 정상입니다."

    if status.failed_checks <= 1:
        return "retry: 일시적 오류일 수 있으므로 재시도합니다."

    if status.failed_checks <= 3:
        return "restart: 반복 실패가 감지되어 서비스 재시작을 요청합니다."

    return "escalate: 자동 복구 한계를 넘어 운영자 확인이 필요합니다."


def main() -> None:
    """여러 서비스 상태에 대한 복구 판단을 출력합니다."""

    statuses = [
        ServiceStatus("backend", True, 0),
        ServiceStatus("backend", False, 1),
        ServiceStatus("worker", False, 3),
        ServiceStatus("monitor", False, 5),
    ]

    for status in statuses:
        print("\n=== Service Status ===")
        print(status)
        print(decide_recovery_action(status))


if __name__ == "__main__":
    main()
