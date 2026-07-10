r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\05_handoff-context-mcp

Run command:
    python .\01_handoff_context_mcp.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 간 Handoff, Context 공유, MCP식 Tool 연결 구조 예제입니다."""

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class AgentContext:
    """Agent 간에 전달되는 최소 실행 Context입니다."""

    request_id: str
    user_request: str
    current_agent: str
    previous_result: str = ""
    handoff_reason: str = ""
    required_action: str = ""
    allowed_tools: list[str] = field(default_factory=list)


@dataclass
class HandoffResult:
    """한 Agent가 처리한 뒤 다음 Agent에게 넘길 결과입니다."""

    next_agent: str
    context: AgentContext
    message: str


def diagnosis_agent(context: AgentContext) -> HandoffResult:
    """장애 원인을 분석하고 복구 Agent에게 넘길 Context를 만듭니다."""

    result = "backend health check 실패, 최근 배포 이후 오류 증가"
    next_context = AgentContext(
        request_id=context.request_id,
        user_request=context.user_request,
        current_agent="recovery_agent",
        previous_result=result,
        handoff_reason="장애 원인이 운영 복구 절차와 관련됨",
        required_action="restart_or_fallback",
        allowed_tools=["restart_service", "read_service_logs"],
    )
    return HandoffResult("recovery_agent", next_context, result)


def recovery_agent(context: AgentContext) -> HandoffResult:
    """허용된 Tool 목록을 확인하고 안전한 복구 조치를 선택합니다."""

    if "restart_service" in context.allowed_tools:
        result = "backend 서비스를 재시작하고 health check를 다시 확인"
    else:
        result = "권한 부족: 운영자 승인 필요"

    next_context = AgentContext(
        request_id=context.request_id,
        user_request=context.user_request,
        current_agent="validation_agent",
        previous_result=result,
        handoff_reason="복구 결과 검증 필요",
        required_action="validate_recovery",
        allowed_tools=["check_health"],
    )
    return HandoffResult("validation_agent", next_context, result)


def validation_agent(context: AgentContext) -> HandoffResult:
    """복구 결과를 검증하고 최종 보고 Agent에게 넘깁니다."""

    result = "health check 정상, 복구 성공으로 판단"
    next_context = AgentContext(
        request_id=context.request_id,
        user_request=context.user_request,
        current_agent="reporter_agent",
        previous_result=result,
        handoff_reason="운영자에게 최종 결과 보고",
        required_action="summarize",
        allowed_tools=[],
    )
    return HandoffResult("reporter_agent", next_context, result)


def reporter_agent(context: AgentContext) -> HandoffResult:
    """운영자에게 전달할 최종 요약을 생성합니다."""

    result = f"[{context.request_id}] 처리 완료: {context.previous_result}"
    return HandoffResult("done", context, result)


def run_handoff_flow(user_request: str) -> list[HandoffResult]:
    """Agent 간 Handoff가 어떤 Context를 전달하는지 순서대로 실행합니다."""

    context = AgentContext(
        request_id="REQ-1001",
        user_request=user_request,
        current_agent="diagnosis_agent",
        allowed_tools=["read_service_logs"],
    )

    agents: dict[str, Callable[[AgentContext], HandoffResult]] = {
        "diagnosis_agent": diagnosis_agent,
        "recovery_agent": recovery_agent,
        "validation_agent": validation_agent,
        "reporter_agent": reporter_agent,
    }

    results: list[HandoffResult] = []
    current_agent = context.current_agent
    while current_agent != "done":
        result = agents[current_agent](context)
        results.append(result)
        context = result.context
        current_agent = result.next_agent

    return results


def main() -> None:
    """Handoff 단계별 Context 변화를 출력합니다."""

    flow = run_handoff_flow("backend 장애가 발생했습니다. 원인 분석과 복구가 필요합니다.")
    for index, result in enumerate(flow, start=1):
        print(f"\n=== Step {index}: next={result.next_agent} ===")
        print(f"message: {result.message}")
        print(f"context: {result.context}")


if __name__ == "__main__":
    main()
