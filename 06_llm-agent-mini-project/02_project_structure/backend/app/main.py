"""FastAPI 애플리케이션 시작 파일입니다.

실행 위치:
    C:\aidev\06_llm-agent-mini-project\team-schedule-agent\backend

실행 명령:
    uvicorn app.main:app --reload

구현할 내용:
    1. FastAPI 앱을 생성합니다.
    2. /health endpoint를 제공합니다.
    3. app.routers.agent_router에 작성한 Agent API router를 등록합니다.
    4. Swagger에서 /agent/schedule endpoint를 테스트할 수 있게 만듭니다.
"""

from fastapi import FastAPI

from app.routers.agent_router import router as agent_router


app = FastAPI(title="Schedule Agent API")


@app.get("/health")
def health_check() -> dict[str, str]:
    """서버가 실행 중인지 확인하는 기본 endpoint입니다."""
    return {"status": "ok"}


app.include_router(agent_router, prefix="/agent", tags=["agent"])
