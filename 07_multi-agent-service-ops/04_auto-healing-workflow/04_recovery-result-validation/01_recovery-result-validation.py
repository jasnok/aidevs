r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow\04_recovery-result-validation

Run command:
    python .\01_recovery-result-validation.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""복구 조치 결과를 검증하고 최종 상태를 판정하는 예제입니다."""

from dataclasses import dataclass
from typing import Literal


ValidationStatus = Literal["recovered", "partially_recovered", "failed"]


@dataclass
class RecoveryValidation:
    """복구 검증 결과를 저장합니다."""

    service_name: str
    status: ValidationStatus
    reason: str
    next_step: str


def validate_recovery(
    service_name: str,
    health_ok: bool,
    error_count_after_action: int,
    user_request_ok: bool,
) -> RecoveryValidation:
    """Health Check, 오류 로그, 사용자 요청 처리 여부로 복구 결과를 판정합니다."""

    if health_ok and error_count_after_action == 0 and user_request_ok:
        return RecoveryValidation(
            service_name,
            "recovered",
            "Health Check, 오류 로그, 사용자 요청 처리 모두 정상입니다.",
            "운영 로그에 복구 완료로 기록합니다.",
        )

    if health_ok and not user_request_ok:
        return RecoveryValidation(
            service_name,
            "partially_recovered",
            "서비스는 살아 있지만 사용자 요청 처리가 실패합니다.",
            "애플리케이션 로그와 API 라우팅을 추가 확인합니다.",
        )

    return RecoveryValidation(
        service_name,
        "failed",
        "복구 후에도 Health Check 또는 오류 로그가 정상화되지 않았습니다.",
        "운영자에게 알리고 수동 대응 절차로 전환합니다.",
    )


def main() -> None:
    """여러 복구 결과 사례를 검증합니다."""

    cases = [
        ("backend", True, 0, True),
        ("frontend", True, 0, False),
        ("worker", False, 3, False),
    ]

    for case in cases:
        print(validate_recovery(*case))


if __name__ == "__main__":
    main()
