r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow\01_failure-scenarios

Run command:
    python .\01_failure-scenario-classifier.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""서비스 장애 메시지를 장애 유형으로 분류하는 예제입니다."""

from dataclasses import dataclass
from typing import Literal


FailureType = Literal[
    "unhealthy",
    "timeout",
    "dependency_error",
    "permission_error",
    "unknown",
]


@dataclass
class FailureScenario:
    """장애 분류 결과와 권장 조치를 저장합니다."""

    failure_type: FailureType
    reason: str
    recommended_action: str


def classify_failure(message: str) -> FailureScenario:
    """로그나 상태 메시지를 보고 장애 유형을 분류합니다."""

    lowered = message.lower()

    if "health" in lowered or "unhealthy" in lowered:
        return FailureScenario("unhealthy", "Health Check 실패", "재시도 후 서비스 재시작")
    if "timeout" in lowered or "timed out" in lowered:
        return FailureScenario("timeout", "응답 시간 초과", "짧은 재시도 후 로그 확인")
    if "database" in lowered or "api" in lowered or "connection" in lowered:
        return FailureScenario("dependency_error", "외부 의존성 연결 실패", "의존 서비스 상태 확인")
    if "permission" in lowered or "unauthorized" in lowered or "secret" in lowered:
        return FailureScenario("permission_error", "권한 또는 Secret 문제", "환경 변수와 권한 설정 확인")

    return FailureScenario("unknown", "알 수 없는 장애", "로그 수집 후 수동 확인")


def main() -> None:
    """여러 장애 메시지를 분류합니다."""

    samples = [
        "backend health check failed",
        "request timed out after 5 seconds",
        "database connection failed",
        "unauthorized secret access",
        "worker stopped unexpectedly",
    ]

    for sample in samples:
        print("\n=== Failure Message ===")
        print(sample)
        print(classify_failure(sample))


if __name__ == "__main__":
    main()
