r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\team-template\backend

Run command:
    uvicorn main:app --reload

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Auto Healing Agent backend API입니다."""

from datetime import datetime
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Auto Healing Agent Backend")

ExecutionStatus = Literal["pending", "running", "success", "failed"]
EVENTS: list[dict] = []


class HealingRequest(BaseModel):
    """Auto Healing 실행 요청 데이터입니다."""

    service_name: str = "backend"
    failure_message: str = "backend health check failed"


class HealingResult(BaseModel):
    """Auto Healing 실행 결과 데이터입니다."""

    execution_id: str
    service_name: str
    failure_type: str
    action: str
    status: ExecutionStatus
    message: str


def classify_failure(message: str) -> str:
    """장애 메시지를 간단한 장애 유형으로 분류합니다."""

    lowered = message.lower()
    if "health" in lowered or "unhealthy" in lowered:
        return "unhealthy"
    if "timeout" in lowered:
        return "timeout"
    if "permission" in lowered or "unauthorized" in lowered:
        return "permission_error"
    if "connection" in lowered or "database" in lowered:
        return "dependency_error"
    return "unknown"


def choose_action(failure_type: str) -> str:
    """장애 유형에 맞는 복구 조치를 선택합니다."""

    return {
        "unhealthy": "restart_service",
        "timeout": "retry_request",
        "permission_error": "escalate_to_operator",
        "dependency_error": "check_dependency",
        "unknown": "collect_logs",
    }.get(failure_type, "collect_logs")


def add_event(service_name: str, event_type: str, status: str, message: str) -> None:
    """운영 이벤트를 메모리에 기록합니다."""

    EVENTS.append(
        {
            "time": datetime.now().strftime("%H:%M:%S"),
            "service_name": service_name,
            "event_type": event_type,
            "status": status,
            "message": message,
        }
    )


@app.get("/health")
def health() -> dict[str, str]:
    """backend 서비스 상태 확인 엔드포인트입니다."""

    return {"status": "ok", "service": "backend"}


@app.post("/heal", response_model=HealingResult)
def heal(request: HealingRequest) -> HealingResult:
    """장애 메시지를 받아 Auto Healing 조치를 결정합니다."""

    execution_id = str(uuid4())
    failure_type = classify_failure(request.failure_message)
    action = choose_action(failure_type)
    message = f"{request.service_name} 장애 유형은 {failure_type}, 권장 조치는 {action}입니다."
    add_event(request.service_name, "auto_healing", "success", message)
    return HealingResult(
        execution_id=execution_id,
        service_name=request.service_name,
        failure_type=failure_type,
        action=action,
        status="success",
        message=message,
    )


@app.get("/events")
def list_events() -> list[dict]:
    """최근 운영 이벤트 목록을 반환합니다."""

    return EVENTS[-20:]
