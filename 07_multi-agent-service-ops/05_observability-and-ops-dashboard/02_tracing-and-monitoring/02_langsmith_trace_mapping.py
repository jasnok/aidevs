r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard\02_tracing-and-monitoring

Run command:
    python .\02_langsmith_trace_mapping.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""LangSmith식 실행 추적 데이터 구조를 이해하기 위한 Mock 예제입니다.

실제 LangSmith API를 호출하지 않고, 수업에서 trace/run/span 개념을
눈으로 확인할 수 있도록 로컬 데이터만 생성합니다.
"""

from dataclasses import dataclass, field
from time import perf_counter, sleep
from uuid import uuid4


@dataclass
class LangSmithLikeRun:
    """LangSmith의 run/span과 비슷한 실행 단위입니다."""

    run_id: str
    parent_run_id: str | None
    name: str
    run_type: str
    status: str
    inputs: dict[str, str]
    outputs: dict[str, str]
    duration_ms: float


@dataclass
class LangSmithLikeTrace:
    """하나의 사용자 요청을 추적하는 trace입니다."""

    trace_id: str
    project_name: str
    user_request: str
    runs: list[LangSmithLikeRun] = field(default_factory=list)

    def add_run(
        self,
        name: str,
        run_type: str,
        inputs: dict[str, str],
        outputs: dict[str, str],
        parent_run_id: str | None = None,
    ) -> str:
        """실행 단계를 trace에 추가하고 run_id를 반환합니다."""

        start = perf_counter()
        sleep(0.03)
        duration_ms = round((perf_counter() - start) * 1000, 2)
        run_id = str(uuid4())
        self.runs.append(
            LangSmithLikeRun(
                run_id=run_id,
                parent_run_id=parent_run_id,
                name=name,
                run_type=run_type,
                status="success",
                inputs=inputs,
                outputs=outputs,
                duration_ms=duration_ms,
            )
        )
        return run_id


def run_multi_agent_trace(user_request: str) -> LangSmithLikeTrace:
    """Multi-Agent 흐름을 LangSmith식 trace 구조로 기록합니다."""

    trace = LangSmithLikeTrace(
        trace_id=str(uuid4()),
        project_name="aidev-06-service-ops",
        user_request=user_request,
    )

    supervisor_run_id = trace.add_run(
        name="supervisor_agent",
        run_type="chain",
        inputs={"request": user_request},
        outputs={"route": "ops_agent"},
    )
    ops_run_id = trace.add_run(
        name="ops_agent",
        run_type="llm",
        inputs={"task": "장애 원인 분석"},
        outputs={"analysis": "backend health check 실패"},
        parent_run_id=supervisor_run_id,
    )
    trace.add_run(
        name="health_check_tool",
        run_type="tool",
        inputs={"url": "http://backend:8000/health"},
        outputs={"status": "failed"},
        parent_run_id=ops_run_id,
    )
    trace.add_run(
        name="reviewer_agent",
        run_type="chain",
        inputs={"analysis": "backend health check 실패"},
        outputs={"decision": "restart 후 재검증"},
        parent_run_id=supervisor_run_id,
    )

    return trace


def main() -> None:
    """LangSmith식 trace 구조를 출력합니다."""

    trace = run_multi_agent_trace("backend 장애 원인을 추적해줘.")
    print(f"trace_id={trace.trace_id}")
    print(f"project={trace.project_name}")
    print(f"request={trace.user_request}")
    for run in trace.runs:
        print("\n=== Run ===")
        print(run)


if __name__ == "__main__":
    main()
