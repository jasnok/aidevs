r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\01_single-vs-multi-agent

Run command:
    python .\01_single-agent-vs-multi-agent.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""단일 Agent와 Multi-Agent 구조를 비교하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class AgentResult:
    """Agent가 처리한 결과를 일정한 형태로 저장합니다."""

    agent_name: str
    output: str


def single_agent(user_request: str) -> AgentResult:
    """하나의 Agent가 요청 분석, 실행, 검토를 모두 처리합니다."""

    output = (
        f"요청 분석: {user_request}\n"
        "실행 계획: 필요한 작업을 한 Agent가 모두 처리합니다.\n"
        "검토 결과: 구조는 단순하지만 역할이 커지면 복잡해질 수 있습니다."
    )
    return AgentResult(agent_name="single_agent", output=output)


def planner_agent(user_request: str) -> AgentResult:
    """Planner Agent는 사용자의 요청을 보고 실행 계획을 만듭니다."""

    return AgentResult(
        agent_name="planner_agent",
        output=f"'{user_request}' 요청을 분석하고 실행 단계를 3개로 나눕니다.",
    )


def executor_agent(plan: str) -> AgentResult:
    """Executor Agent는 Planner가 만든 계획을 실제 작업 결과로 바꿉니다."""

    return AgentResult(
        agent_name="executor_agent",
        output=f"계획을 실행합니다: {plan}",
    )


def reviewer_agent(result: str) -> AgentResult:
    """Reviewer Agent는 실행 결과의 품질과 누락된 내용을 확인합니다."""

    return AgentResult(
        agent_name="reviewer_agent",
        output=f"결과를 검토했습니다. 개선 필요 여부: 낮음. 검토 대상: {result}",
    )


def multi_agent(user_request: str) -> list[AgentResult]:
    """여러 Agent가 각자의 역할을 맡아 순서대로 협업합니다."""

    plan = planner_agent(user_request)
    execution = executor_agent(plan.output)
    review = reviewer_agent(execution.output)
    return [plan, execution, review]


def main() -> None:
    """예제를 실행하고 두 구조의 출력 차이를 확인합니다."""

    user_request = "장애가 난 AI 서비스를 복구하는 절차를 알려줘"

    print("=== Single Agent ===")
    print(single_agent(user_request).output)

    print("\n=== Multi-Agent ===")
    for result in multi_agent(user_request):
        print(f"[{result.agent_name}] {result.output}")


if __name__ == "__main__":
    main()
