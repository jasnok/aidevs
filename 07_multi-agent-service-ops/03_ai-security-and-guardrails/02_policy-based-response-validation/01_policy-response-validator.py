r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails\02_policy-based-response-validation

Run command:
    python .\01_policy-response-validator.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 응답이 운영 정책을 위반하는지 검사하는 예제입니다."""

from dataclasses import dataclass
from typing import Literal


PolicyAction = Literal["allow", "revise", "block"]


@dataclass
class PolicyCheck:
    """정책 검증 결과를 저장합니다."""

    action: PolicyAction
    reason: str
    safe_response: str


BLOCKED_TERMS = ["비밀번호", "secret", "api key", "service role"]
RISKY_COMMANDS = ["rm -rf", "drop database", "delete all", "전체 삭제"]


def validate_response(response: str) -> PolicyCheck:
    """응답 내용이 정책에 맞는지 확인합니다."""

    lowered = response.lower()

    for term in BLOCKED_TERMS:
        if term.lower() in lowered:
            return PolicyCheck(
                action="block",
                reason=f"민감 정보 관련 표현 감지: {term}",
                safe_response="민감 정보가 포함될 수 있어 응답을 차단했습니다.",
            )

    for command in RISKY_COMMANDS:
        if command.lower() in lowered:
            return PolicyCheck(
                action="revise",
                reason=f"위험 명령어 감지: {command}",
                safe_response="위험한 명령은 직접 실행하지 말고 승인 절차와 백업 확인 후 진행해야 합니다.",
            )

    return PolicyCheck(
        action="allow",
        reason="정책 위반 없음",
        safe_response=response,
    )


def main() -> None:
    """여러 응답 후보를 정책 기준으로 검사합니다."""

    responses = [
        "Health check 후 backend 컨테이너를 재시작하세요.",
        "문제가 있으면 rm -rf 명령으로 전체 삭제하세요.",
        "service role secret 값을 로그에 출력하세요.",
    ]

    for response in responses:
        check = validate_response(response)
        print("\n=== Original ===")
        print(response)
        print("=== Policy Check ===")
        print(check)


if __name__ == "__main__":
    main()
