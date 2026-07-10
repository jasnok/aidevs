# Sample Schedule Agent

이 샘플은 LangGraph, Tool, State, Streamlit을 하나로 연결한 일정 조정 Agent 예제입니다.

실제 캘린더 API는 사용하지 않고 Mock 데이터를 사용합니다. 먼저 Mock 데이터로 Agent 흐름을 이해한 뒤, 필요한 경우 실제 외부 API나 RAG/Memory 구조를 연결합니다.

## 구성

```text
sample-schedule-agent
├─ .env.example
├─ README.md
├─ requirements.txt
├─ app
│  ├─ __init__.py
│  ├─ graph.py
│  ├─ mock_data.py
│  ├─ schemas.py
│  └─ tools.py
├─ docs
│  ├─ agent-flow.md
│  ├─ test-checklist.md
│  └─ tool-spec.md
└─ frontend
   └─ streamlit_app.py
```

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python -m app.graph
```

화면으로 확인하려면 다음 명령을 실행합니다.

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8601
```

## 확인 포인트

- State에 어떤 값이 저장되는지 확인합니다.
- Tool 함수가 어떤 순서로 호출되는지 확인합니다.
- Agent가 최종 제안 메시지를 어떻게 만드는지 확인합니다.
- OpenAI API Key가 없을 때 규칙 기반 응답으로 대체되는 흐름을 확인합니다.
- 오류가 발생했을 때 어느 단계에서 멈췄는지 기록합니다.
