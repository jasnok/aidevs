r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard\02_tracing-and-monitoring

Run command:
    python .\01_trace-agent-execution.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Agent 실행 흐름을 Trace로 기록하는 예제입니다."""

from dataclasses import dataclass, field
from time import perf_counter, sleep
from uuid import uuid4


@dataclass
class TraceStep:
    """Trace 안에서 실행된 한 단계를 표현합니다."""

    step_name: str
    status: str
    duration_ms: float
    detail: str


@dataclass
class ExecutionTrace:
    """하나의 사용자 요청에 대한 전체 실행 추적 정보입니다."""

    trace_id: str
    request: str
    steps: list[TraceStep] = field(default_factory=list)

    def add_step(self, step_name: str, status: str, duration_ms: float, detail: str) -> None:
        """Trace에 실행 단계를 추가합니다."""

        self.steps.append(TraceStep(step_name, status, duration_ms, detail))


def run_step(trace: ExecutionTrace, step_name: str, detail: str) -> None:
    """샘플 실행 단계를 수행하고 걸린 시간을 기록합니다."""

    start = perf_counter()
    sleep(0.05)
    duration_ms = (perf_counter() - start) * 1000
    trace.add_step(step_name, "success", round(duration_ms, 2), detail)


def run_agent_flow(request: str) -> ExecutionTrace:
    """Multi-Agent 실행 흐름을 Trace로 기록합니다."""

    trace = ExecutionTrace(trace_id=str(uuid4()), request=request)
    run_step(trace, "supervisor_agent", "요청 유형 분류")
    run_step(trace, "ops_agent", "서비스 상태 점검")
    run_step(trace, "tool_health_check", "health check tool 실행")
    run_step(trace, "reviewer_agent", "응답 품질 검토")
    return trace


def main() -> None:
    """샘플 요청의 Trace를 출력합니다."""

    trace = run_agent_flow("backend 장애 여부를 확인해줘")
    print(f"trace_id={trace.trace_id}")
    print(f"request={trace.request}")
    for step in trace.steps:
        print(step)


if __name__ == "__main__":
    main()
