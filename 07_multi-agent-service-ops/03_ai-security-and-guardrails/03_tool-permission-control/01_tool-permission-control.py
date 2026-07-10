r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails\03_tool-permission-control

Run command:
    python .\01_tool-permission-control.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 역할별 Tool 실행 권한을 제어하는 예제입니다."""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Tool:
    """Agent가 사용할 수 있는 Tool 정의입니다."""

    name: str
    description: str
    run: Callable[[str], str]


ROLE_PERMISSIONS = {
    "viewer_agent": {"read_logs", "check_health"},
    "ops_agent": {"read_logs", "check_health", "restart_service"},
    "security_agent": {"read_logs", "check_health", "block_user"},
}


def read_logs(service_name: str) -> str:
    """서비스 로그를 조회합니다."""

    return f"{service_name} 로그를 조회했습니다. 최근 오류 0건."


def check_health(service_name: str) -> str:
    """서비스 Health Check 상태를 확인합니다."""

    return f"{service_name} health status: ok"


def restart_service(service_name: str) -> str:
    """서비스 재시작 요청을 생성합니다."""

    return f"{service_name} 재시작 요청을 생성했습니다."


def block_user(user_id: str) -> str:
    """위험 사용자를 차단합니다."""

    return f"사용자 {user_id} 차단 요청을 생성했습니다."


TOOLS = {
    "read_logs": Tool("read_logs", "서비스 로그 조회", read_logs),
    "check_health": Tool("check_health", "서비스 상태 확인", check_health),
    "restart_service": Tool("restart_service", "서비스 재시작", restart_service),
    "block_user": Tool("block_user", "사용자 차단", block_user),
}


def execute_tool(agent_role: str, tool_name: str, argument: str) -> str:
    """Agent 역할이 Tool 실행 권한을 가지고 있는지 확인한 뒤 실행합니다."""

    allowed_tools = ROLE_PERMISSIONS.get(agent_role, set())
    if tool_name not in allowed_tools:
        return f"권한 거부: {agent_role}는 {tool_name} Tool을 실행할 수 없습니다."

    tool = TOOLS[tool_name]
    return tool.run(argument)


def main() -> None:
    """역할별 Tool 실행 결과를 비교합니다."""

    scenarios = [
        ("viewer_agent", "read_logs", "backend"),
        ("viewer_agent", "restart_service", "backend"),
        ("ops_agent", "restart_service", "backend"),
        ("security_agent", "block_user", "user-123"),
    ]

    for role, tool_name, argument in scenarios:
        print("\n=== Tool Request ===")
        print(f"role={role}, tool={tool_name}, argument={argument}")
        print(execute_tool(role, tool_name, argument))


if __name__ == "__main__":
    main()
