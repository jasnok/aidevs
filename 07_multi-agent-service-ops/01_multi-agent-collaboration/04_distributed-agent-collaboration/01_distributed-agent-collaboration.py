r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration\04_distributed-agent-collaboration

Run command:
    python .\01_distributed-agent-collaboration.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""분산 Multi-Agent 협업 구조를 단순화해서 보여주는 예제입니다."""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass


@dataclass
class CollaborationResult:
    """각 Agent가 반환한 결과와 품질 점수를 저장합니다."""

    agent_name: str
    summary: str
    confidence: float


def infra_agent(service_name: str) -> CollaborationResult:
    """인프라 Agent는 서비스 상태와 배포 환경을 점검합니다."""

    return CollaborationResult(
        agent_name="infra_agent",
        summary=f"{service_name} 컨테이너 상태와 포트 바인딩을 확인해야 합니다.",
        confidence=0.86,
    )


def app_agent(service_name: str) -> CollaborationResult:
    """애플리케이션 Agent는 API 응답과 예외 로그를 점검합니다."""

    return CollaborationResult(
        agent_name="app_agent",
        summary=f"{service_name} 애플리케이션 로그에서 최근 예외를 확인해야 합니다.",
        confidence=0.91,
    )


def security_agent(service_name: str) -> CollaborationResult:
    """보안 Agent는 권한과 위험한 입력 여부를 점검합니다."""

    return CollaborationResult(
        agent_name="security_agent",
        summary=f"{service_name}의 관리자 API 접근 권한을 확인해야 합니다.",
        confidence=0.78,
    )


def merge_results(results: list[CollaborationResult]) -> str:
    """여러 Agent 결과를 운영자가 읽기 쉬운 하나의 보고서로 합칩니다."""

    lines = ["Multi-Agent 협업 결과"]
    for result in results:
        lines.append(f"- {result.agent_name}: {result.summary} (confidence={result.confidence})")
    lines.append("권장 조치: 인프라 상태, 앱 로그, 권한 설정을 순서대로 확인합니다.")
    return "\n".join(lines)


def main() -> None:
    """여러 Agent를 병렬로 실행하고 결과를 통합합니다."""

    service_name = "ai-support-backend"
    agents = [infra_agent, app_agent, security_agent]

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(lambda agent: agent(service_name), agents))

    print(merge_results(results))


if __name__ == "__main__":
    main()
