r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow\03_recovery-pipeline

Run command:
    python .\01_auto-healing-pipeline.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Auto Healing 파이프라인을 순서대로 실행하는 예제입니다."""

from dataclasses import dataclass, field
from typing import Literal


Action = Literal["none", "retry", "restart", "escalate"]


@dataclass
class HealingState:
    """Auto Healing 과정에서 공유되는 상태입니다."""

    service_name: str
    health_message: str
    failure_type: str = "unknown"
    action: Action = "none"
    result: str = "pending"
    events: list[str] = field(default_factory=list)


def classify_failure(state: HealingState) -> HealingState:
    """상태 메시지를 기반으로 장애 유형을 저장합니다."""

    lowered = state.health_message.lower()
    if "timeout" in lowered:
        state.failure_type = "timeout"
    elif "health" in lowered or "unhealthy" in lowered:
        state.failure_type = "unhealthy"
    elif "connection" in lowered:
        state.failure_type = "dependency_error"
    else:
        state.failure_type = "unknown"
    state.events.append(f"failure classified: {state.failure_type}")
    return state


def choose_action(state: HealingState) -> HealingState:
    """장애 유형에 맞는 복구 조치를 선택합니다."""

    action_map: dict[str, Action] = {
        "timeout": "retry",
        "unhealthy": "restart",
        "dependency_error": "escalate",
        "unknown": "escalate",
    }
    state.action = action_map.get(state.failure_type, "escalate")
    state.events.append(f"action selected: {state.action}")
    return state


def execute_action(state: HealingState) -> HealingState:
    """선택된 복구 조치를 Mock 방식으로 실행합니다."""

    messages = {
        "none": "조치 없음",
        "retry": "요청 재시도 완료",
        "restart": f"{state.service_name} 재시작 요청 완료",
        "escalate": "운영자 확인 필요",
    }
    state.result = messages[state.action]
    state.events.append(f"action executed: {state.result}")
    return state


def run_pipeline(service_name: str, health_message: str) -> HealingState:
    """Auto Healing 파이프라인 전체를 실행합니다."""

    state = HealingState(service_name=service_name, health_message=health_message)
    state.events.append("pipeline started")
    state = classify_failure(state)
    state = choose_action(state)
    state = execute_action(state)
    state.events.append("pipeline finished")
    return state


def main() -> None:
    """샘플 장애에 대해 Auto Healing 파이프라인을 실행합니다."""

    state = run_pipeline("backend", "backend health check failed")
    print(state)
    print("\nEvent Log")
    for event in state.events:
        print(f"- {event}")


if __name__ == "__main__":
    main()
