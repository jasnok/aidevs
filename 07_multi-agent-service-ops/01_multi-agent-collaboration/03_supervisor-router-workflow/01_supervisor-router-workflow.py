r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\03_supervisor-router-workflow

Run command:
    python .\01_supervisor-router-workflow.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Supervisor/Router가 Agent 작업을 분배하는 예제입니다."""

from typing import Literal, TypedDict


class AgentState(TypedDict):
    """Agent 협업 중 공유되는 실행 상태입니다."""

    user_request: str
    route: str
    result: str
    status: str


def route_request(user_request: str) -> Literal["ops", "security", "general"]:
    """사용자 요청의 키워드를 보고 담당 Agent를 선택합니다."""

    lowered = user_request.lower()
    if "장애" in user_request or "복구" in user_request or "restart" in lowered:
        return "ops"
    if "보안" in user_request or "권한" in user_request or "injection" in lowered:
        return "security"
    return "general"


def ops_agent(user_request: str) -> str:
    """운영 Agent는 장애 대응과 복구 절차를 담당합니다."""

    return f"운영 대응: health check 후 필요하면 restart/retry를 수행합니다. 요청: {user_request}"


def security_agent(user_request: str) -> str:
    """보안 Agent는 위험 입력과 권한 문제를 점검합니다."""

    return f"보안 검토: 입력 검증과 권한 확인이 필요합니다. 요청: {user_request}"


def general_agent(user_request: str) -> str:
    """일반 Agent는 특정 분류에 속하지 않는 요청을 처리합니다."""

    return f"일반 응답: 요청을 확인했습니다. 요청: {user_request}"


def supervisor(user_request: str) -> AgentState:
    """Router 결과를 보고 적절한 Agent를 실행한 뒤 상태를 반환합니다."""

    route = route_request(user_request)
    handlers = {
        "ops": ops_agent,
        "security": security_agent,
        "general": general_agent,
    }
    result = handlers[route](user_request)

    return {
        "user_request": user_request,
        "route": route,
        "result": result,
        "status": "completed",
    }


def main() -> None:
    """여러 요청을 Supervisor에 전달해 라우팅 결과를 확인합니다."""

    requests = [
        "API 서버 장애가 발생했어. 복구 절차를 알려줘.",
        "사용자 입력에서 prompt injection을 어떻게 막아?",
        "오늘 작업 현황을 요약해줘.",
    ]

    for request in requests:
        state = supervisor(request)
        print("\n=== Supervisor Result ===")
        print(state)


if __name__ == "__main__":
    main()
