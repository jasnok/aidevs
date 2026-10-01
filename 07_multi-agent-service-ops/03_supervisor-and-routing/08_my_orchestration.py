"""이사 준비 Supervisor–Worker 실습. 과정 루트에서 이 파일을 실행한다."""
import json
from pathlib import Path
from typing import Literal
from uuid import uuid4

import yaml
from pydantic import BaseModel, Field
from shared.travel_llm import run_with_metadata

PLAN = ("move_scope_agent", "move_action_agent", "move_timeline_agent")


class Item(BaseModel):
    item_id: str
    name: str
    decision: Literal["move", "sell", "dispose", "undecided"]
    user_status: str = "미확인"


class Service(BaseModel):
    service_id: str
    kind: str
    user_status: str = "미확인"


class MoveRequest(BaseModel):
    moving_date: str
    origin_city: str
    destination_city: str
    items: list[Item] = Field(min_length=1)
    services: list[Service] = Field(default_factory=list)
    access_constraints: list[str] = Field(default_factory=list)


class SupervisorDecision(BaseModel):
    agent_id: Literal["supervisor_agent"] = "supervisor_agent"
    next_agent: Literal["move_scope_agent", "move_action_agent", "move_timeline_agent", "finish"]
    reason: str


class MoveScopeResult(BaseModel):
    agent_id: Literal["move_scope_agent"] = "move_scope_agent"
    items: list[Item]
    services: list[Service]
    access_constraints: list[str]


class Action(BaseModel):
    task_id: str
    target_ids: list[str] = Field(min_length=1)
    description: str = Field(min_length=1)
    phase: Literal["before", "moving_day", "after"]


class NoAction(BaseModel):
    target_id: str
    reason: str = Field(min_length=1)


class MoveActionPlanResult(BaseModel):
    agent_id: Literal["move_action_agent"] = "move_action_agent"
    tasks: list[Action]
    no_action_targets: list[NoAction] = Field(default_factory=list)
    confirmations: list[str] = Field(default_factory=list)


class Step(BaseModel):
    order: int = Field(ge=1)
    phase: Literal["before", "moving_day", "after"]
    task_ids: list[str]
    description: str = Field(min_length=1)


class MoveTimelineResult(BaseModel):
    agent_id: Literal["move_timeline_agent"] = "move_timeline_agent"
    steps: list[Step]
    covered_target_ids: list[str]
    unverified_items: list[str] = Field(default_factory=list)


CONTRACTS = {
    "MoveScopeResult": MoveScopeResult,
    "MoveActionPlanResult": MoveActionPlanResult,
    "MoveTimelineResult": MoveTimelineResult,
}


def load_workers() -> dict:
    path = Path(__file__).resolve().with_name("my_worker_definiitons.yaml")
    workers = yaml.safe_load(path.read_text(encoding="utf-8"))["workers"]
    required = {"name", "goal", "instructions", "provider", "output_contract"}
    if set(workers) != set(PLAN):
        raise ValueError("YAML과 실행 계획의 Worker ID가 다릅니다.")
    for agent_id, worker in workers.items():
        if not required <= worker.keys() or worker["output_contract"] not in CONTRACTS:
            raise ValueError(f"{agent_id} Worker 설정이 유효하지 않습니다.")
    return workers


WORKERS = load_workers()


def records(rows, id_field):
    ids = [getattr(row, id_field) for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("ID가 중복됐습니다.")
    return {getattr(row, id_field): row.model_dump() for row in rows}


def verify(agent_id: str, payload: dict, request: MoveRequest, outputs: dict) -> dict:
    result = CONTRACTS[WORKERS[agent_id]["output_contract"]].model_validate(payload)
    targets = {x.item_id for x in request.items} | {x.service_id for x in request.services}
    if agent_id == "move_scope_agent":
        if records(result.items, "item_id") != records(request.items, "item_id"):
            raise ValueError("물품의 누락·추가 또는 상태 변경")
        if records(result.services, "service_id") != records(request.services, "service_id"):
            raise ValueError("서비스의 누락·추가 또는 상태 변경")
        if result.access_constraints != request.access_constraints:
            raise ValueError("현장 제약 변경")
    elif agent_id == "move_action_agent":
        task_ids = [task.task_id for task in result.tasks]
        if len(task_ids) != len(set(task_ids)):
            raise ValueError("중복된 작업 ID")
        referenced = {x for task in result.tasks for x in task.target_ids}
        no_action = [x.target_id for x in result.no_action_targets]
        if len(no_action) != len(set(no_action)) or referenced & set(no_action):
            raise ValueError("작업 있음/없음 표시가 모순됩니다.")
        if referenced | set(no_action) != targets:
            raise ValueError("물품·서비스 대상이 누락·추가됐습니다.")
    else:
        actions = MoveActionPlanResult.model_validate(outputs["move_action_agent"])
        expected_tasks = {task.task_id for task in actions.tasks}
        used = [x for step in result.steps for x in step.task_ids]
        if set(used) != expected_tasks or len(used) != len(set(used)):
            raise ValueError("최종 일정의 작업 ID가 누락·중복·추가됐습니다.")
        if [s.order for s in result.steps] != list(range(1, len(result.steps) + 1)):
            raise ValueError("일정 순서가 연속되지 않습니다.")
        if set(result.covered_target_ids) != targets or len(result.covered_target_ids) != len(targets):
            raise ValueError("최종 결과의 물품·서비스 ID가 누락·추가됐습니다.")
        phases = {task.task_id: task.phase for task in actions.tasks}
        if any(step.phase != phases[x] for step in result.steps for x in step.task_ids):
            raise ValueError("작업 시점이 앞 계약과 다릅니다.")
    return result.model_dump()


def supervisor_agent(request: MoveRequest, completed: list[str], expected: str) -> dict:
    prompt = (
        "당신은 supervisor_agent입니다. 업무 결과를 직접 작성하지 마세요.\n"
        "순서: move_scope_agent → move_action_agent → move_timeline_agent → finish\n"
        f"완료된 Worker: {completed}\n허용된 다음 행동: {expected}\n"
        f"사용자 입력: {request.model_dump_json()}\nSupervisorDecision JSON으로 결정하세요."
    )
    return run_with_metadata("openai", prompt, SupervisorDecision)


def selected_worker_agent(agent_id: str, request: MoveRequest, context: dict) -> dict:
    worker = WORKERS[agent_id]
    prompt = (
        f"당신은 {agent_id}입니다.\n이름: {worker['name']}\n"
        f"Goal: {worker['goal']}\nInstructions: {worker['instructions']}\n"
        f"사용자 입력: {request.model_dump_json()}\n"
        f"검증된 이전 결과: {json.dumps(context, ensure_ascii=False)}\n"
        f"{worker['output_contract']} JSON으로 반환하세요. agent_id는 {agent_id}입니다."
    )
    return run_with_metadata(worker["provider"], prompt, CONTRACTS[worker["output_contract"]])


def my_orchestration(request: MoveRequest | dict, max_llm_calls: int = 7) -> dict:
    request = MoveRequest.model_validate(request)
    ids = [x.item_id for x in request.items] + [x.service_id for x in request.services]
    if len(ids) != len(set(ids)):
        raise ValueError("입력 ID가 중복됐습니다.")
    state = {"completed_agents": [], "outputs": {}}
    trace = []
    run_id = f"moving-{uuid4().hex[:12]}"

    def record(actor, action, error=None):
        trace.append({"step": len(trace) + 1, "actor": actor, "action": action, "error": error})

    def stop(reason, error=None):
        return {"run_id": run_id, "status": "failed", "reason": reason,
                "error": error, "state": state, "trace": trace}

    llm_calls = 0
    while llm_calls < max_llm_calls:
        completed = state["completed_agents"]
        expected = PLAN[len(completed)] if len(completed) < len(PLAN) else "finish"
        decision = supervisor_agent(request, completed, expected)
        llm_calls += 1
        record("supervisor_agent", "decision", decision["error"])
        if decision["error"] or decision["result"] is None:
            return stop("supervisor_failed", decision["error"])
        selected = decision["result"]["next_agent"]
        if selected != expected:
            return stop("invalid_transition", f"expected={expected}, actual={selected}")
        if selected == "finish":
            return {"run_id": run_id, "status": "completed", "reason": "all_contracts_verified",
                    "state": state, "trace": trace}
        if llm_calls >= max_llm_calls:
            break
        context = {key: state["outputs"][key] for key in completed}
        worker = selected_worker_agent(selected, request, context)
        llm_calls += 1
        record(selected, "worker_completed" if worker["result"] else "worker_failed", worker["error"])
        if worker["error"] or worker["result"] is None:
            return stop("worker_failed", worker["error"])
        try:
            verified = verify(selected, worker["result"], request, state["outputs"])
        except (ValueError, KeyError) as error:
            record("contract_guard", "rejected", str(error))
            return stop("contract_rejected", str(error))
        record("contract_guard", "verified")
        state["outputs"][selected] = verified
        completed.append(selected)
    return stop("max_llm_calls")


if __name__ == "__main__":
    example = MoveRequest(
        moving_date="2026-10-10", origin_city="서울", destination_city="인천",
        items=[
            Item(item_id="item_01", name="책", decision="move"),
            Item(item_id="item_02", name="책상", decision="sell"),
            Item(item_id="item_03", name="에어컨", decision="move"),
        ],
        services=[
            Service(service_id="service_01", kind="용달 예약", user_status="미예약"),
            Service(service_id="service_02", kind="도시가스 전출", user_status="미신청"),
            Service(service_id="service_03", kind="인터넷 이전 설치", user_status="미신청"),
            Service(service_id="service_04", kind="에어컨 철거", user_status="미예약"),
        ],
        access_constraints=["출발지 엘리베이터 없음"],
    )
    print(json.dumps(my_orchestration(example), ensure_ascii=False, indent=2))
