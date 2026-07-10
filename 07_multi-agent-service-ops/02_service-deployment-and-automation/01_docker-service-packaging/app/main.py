r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging\app

Run command:
    uvicorn app.main:app --reload

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Docker 이미지로 패키징할 최소 FastAPI 서비스입니다."""

from fastapi import FastAPI


app = FastAPI(title="AI Service Packaging Demo")


@app.get("/health")
def health() -> dict[str, str]:
    """컨테이너가 정상적으로 실행 중인지 확인하는 엔드포인트입니다."""

    return {"status": "ok", "service": "packaging-demo"}


@app.get("/agent/summary")
def agent_summary() -> dict[str, str]:
    """나중에 Agent 실행 결과가 들어갈 API 형태를 미리 보여줍니다."""

    return {
        "agent": "demo_agent",
        "summary": "Docker로 실행되는 AI 서비스 API입니다.",
    }
