r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails\04_multi-agent-access-control

Run command:
    python .\01_multi-agent-access-control.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Multi-Agent 환경에서 Agent별 데이터 접근 권한을 검사하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class Resource:
    """Agent가 접근하려는 데이터나 기능을 표현합니다."""

    name: str
    required_scope: str


AGENT_SCOPES = {
    "planner_agent": {"read_public_status"},
    "ops_agent": {"read_public_status", "read_ops_logs", "request_restart"},
    "security_agent": {"read_public_status", "read_security_events"},
    "admin_agent": {
        "read_public_status",
        "read_ops_logs",
        "read_security_events",
        "request_restart",
        "approve_risky_action",
    },
}


RESOURCES = {
    "service_status": Resource("service_status", "read_public_status"),
    "ops_logs": Resource("ops_logs", "read_ops_logs"),
    "security_events": Resource("security_events", "read_security_events"),
    "restart_request": Resource("restart_request", "request_restart"),
    "dangerous_action_approval": Resource("dangerous_action_approval", "approve_risky_action"),
}


def can_access(agent_name: str, resource_name: str) -> bool:
    """Agent가 특정 Resource에 접근할 권한이 있는지 검사합니다."""

    scopes = AGENT_SCOPES.get(agent_name, set())
    resource = RESOURCES[resource_name]
    return resource.required_scope in scopes


def explain_access(agent_name: str, resource_name: str) -> str:
    """접근 허용 또는 거부 사유를 사람이 읽을 수 있게 반환합니다."""

    resource = RESOURCES[resource_name]
    if can_access(agent_name, resource_name):
        return f"허용: {agent_name}는 {resource.name}에 접근할 수 있습니다."
    return (
        f"거부: {agent_name}는 {resource.name}에 접근할 수 없습니다. "
        f"필요 권한: {resource.required_scope}"
    )


def main() -> None:
    """여러 Agent와 Resource 조합의 접근 결과를 확인합니다."""

    checks = [
        ("planner_agent", "service_status"),
        ("planner_agent", "ops_logs"),
        ("ops_agent", "restart_request"),
        ("security_agent", "dangerous_action_approval"),
        ("admin_agent", "dangerous_action_approval"),
    ]

    for agent_name, resource_name in checks:
        print(explain_access(agent_name, resource_name))


if __name__ == "__main__":
    main()
