# Backend

이 폴더는 일정 조정 Agent backend starter입니다.

## 역할

- FastAPI endpoint 제공
- LangGraph Agent 실행
- Tool 함수 호출
- Agent 실행 결과와 오류 정보를 응답으로 반환

## 실행 예시

```powershell
cd C:\aidev\06_llm-agent-mini-project\team-schedule-agent\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## 구현할 파일

| 파일 | 해야 할 일 |
| --- | --- |
| `app/main.py` | FastAPI 앱 생성, router 등록, `/health` endpoint 구성 |
| `app/core/config.py` | `.env` 값 읽기, 모델명과 API Key 관리 |
| `app/schemas/agent_state.py` | Agent State와 요청/응답 모델 정의 |
| `app/tools/schedule_tools.py` | 일정 조회, 가능 시간 탐색, 메시지 생성 Tool 구현 |
| `app/graph/schedule_graph.py` | LangGraph Node, Edge, 분기 조건 구현 |
| `app/services/agent_service.py` | API 요청을 받아 graph 실행 |
| `app/routers/agent_router.py` | `/agent/schedule` 같은 endpoint 제공 |
| `tests/test_agent_flow.py` | 정상, 정보 부족, 충돌, Tool 오류 테스트 |
