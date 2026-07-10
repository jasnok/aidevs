# 02_project_structure

이 폴더는 최종 팀 프로젝트를 시작할 때 참고하거나 복사해서 사용하는 starter 구조입니다.

완성 코드가 아니라, 학생들이 직접 구현해야 할 위치를 안내하는 기본 뼈대입니다.

## 구조

```text
02_project_structure
├─ README.md
├─ backend
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ app
│  │  ├─ main.py
│  │  ├─ core
│  │  ├─ graph
│  │  ├─ routers
│  │  ├─ schemas
│  │  ├─ services
│  │  └─ tools
│  └─ tests
├─ frontend
│  ├─ README.md
│  ├─ requirements.txt
│  └─ app.py
└─ docs
   ├─ agent-architecture.md
   ├─ agent-test-report.md
   └─ deployment-note.md
```

## 사용 방법

```powershell
cd C:\aidev\06_llm-agent-mini-project
Copy-Item .\02_project_structure .\team-schedule-agent -Recurse
```

복사한 뒤 `team-schedule-agent` 안에서 구현합니다.

## 구현 순서 추천

1. `docs/agent-architecture.md`에 StateGraph 초안을 먼저 작성합니다.
2. `backend/app/schemas/agent_state.py`에 State 필드를 정의합니다.
3. `backend/app/tools/schedule_tools.py`에 Mock data 기반 Tool을 만듭니다.
4. `backend/app/graph/schedule_graph.py`에 LangGraph Node와 Edge를 연결합니다.
5. `backend/app/routers/agent_router.py`에 API endpoint를 만듭니다.
6. `frontend/app.py`에서 사용자 요청 입력과 결과 출력을 연결합니다.
7. `docs/agent-test-report.md`에 테스트 결과를 기록합니다.
