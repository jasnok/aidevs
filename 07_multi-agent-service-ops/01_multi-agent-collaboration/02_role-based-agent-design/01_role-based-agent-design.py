r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\02_role-based-agent-design

Run command:
    python .\01_role-based-agent-design.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""역할 기반 Agent 설계를 연습하는 예제입니다."""

from dataclasses import dataclass
from typing import Callable


@dataclass
class RoleAgent:
    """역할 이름, 책임, 실행 함수를 하나로 묶은 Agent 정의입니다."""

    name: str
    responsibility: str
    run: Callable[[str], str]


def analyze_request(user_request: str) -> str:
    """요청에서 핵심 의도를 뽑아냅니다."""

    return f"의도 분석 결과: '{user_request}'는 운영 장애 대응 요청입니다."


def plan_recovery(analysis: str) -> str:
    """분석 결과를 바탕으로 복구 계획을 작성합니다."""

    return f"복구 계획: health check -> restart -> retry -> 결과 검증. 근거: {analysis}"


def check_policy(plan: str) -> str:
    """계획이 운영 정책과 보안 기준을 벗어나지 않는지 확인합니다."""

    return f"정책 검토 완료: 위험 작업은 승인 후 실행해야 합니다. 검토 대상: {plan}"


def main() -> None:
    """역할별 Agent를 등록하고 순서대로 실행합니다."""

    agents = [
        RoleAgent("analyst_agent", "사용자 요청의 의도 분석", analyze_request),
        RoleAgent("planner_agent", "복구 절차 계획", plan_recovery),
        RoleAgent("policy_agent", "보안과 운영 정책 검토", check_policy),
    ]

    state = "API 서버가 응답하지 않아요. 자동 복구 절차를 제안해줘."

    for agent in agents:
        print(f"\n[{agent.name}]")
        print(f"책임: {agent.responsibility}")
        state = agent.run(state)
        print(state)


if __name__ == "__main__":
    main()
