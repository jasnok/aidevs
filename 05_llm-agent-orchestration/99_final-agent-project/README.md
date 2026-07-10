# 99 Agent Mini Project

이 폴더는 `05_llm-agent-orchestration` 과정에서 배운 내용을 하나의 미니 프로젝트로 통합하는 단계입니다.

Prompt, Tool Calling, RAG 또는 Memory, LangGraph State Flow를 사용해 일정 조정 Agent를 만들고 실행 결과를 검증합니다.

## 프로젝트 목표

- Agent가 해결할 문제를 명확히 정의합니다.
- StateGraph의 Node, Edge, State를 설계합니다.
- 필요한 Tool을 Python 함수로 구현합니다.
- Tool 선택, Tool 호출, 결과 검증, Retry 또는 Fallback 흐름을 만듭니다.
- Streamlit 화면 또는 CLI에서 Agent 실행 결과를 확인합니다.
- 최종 발표 자료에서 설계 의도와 테스트 결과를 설명합니다.

## 폴더 구성

```text
99_final-agent-project
├─ README.md
├─ sample-schedule-agent
│  ├─ .env.example
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ app
│  │  ├─ __init__.py
│  │  ├─ graph.py
│  │  ├─ mock_data.py
│  │  ├─ schemas.py
│  │  └─ tools.py
│  ├─ docs
│  │  ├─ agent-flow.md
│  │  ├─ test-checklist.md
│  │  └─ tool-spec.md
│  └─ frontend
│     └─ streamlit_app.py
└─ team-template
   ├─ README.md
   ├─ backend
   │  ├─ agent_state.py
   │  ├─ graph.py
   │  ├─ requirements.txt
   │  └─ tools.py
   ├─ docs
   │  ├─ agent-design.md
   │  ├─ project-plan.md
   │  └─ test-checklist.md
   ├─ frontend
   │  └─ app.py
   └─ presentation
      └─ final-presentation.md
```

## 샘플 프로젝트 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python -m app.graph
```

Streamlit 화면으로 확인하려면 다음 명령을 실행합니다.

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8601
```

## 팀 템플릿 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\99_final-agent-project\team-template
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\backend\requirements.txt
python .\backend\graph.py
streamlit run .\frontend\app.py --server.port 8602
```

## 제출물 기준

최종 결과물에는 다음 내용이 포함되어야 합니다.

- Agent가 해결하려는 문제
- State 필드 설계
- Node와 Edge 흐름
- Tool 목록과 입력/출력
- Memory 또는 RAG 사용 여부
- Retry, Fallback, Self-Reflection 전략
- 실행 화면과 테스트 결과
- 개선 전후 비교 또는 한계점

## 확인 질문

- 이 Agent는 어떤 문제를 해결하는가?
- Tool이 2개 이상 필요한 이유는 무엇인가?
- Agent가 잘못 판단했을 때 어떻게 다시 시도하는가?
- State에 불필요한 정보가 너무 많이 들어가지는 않는가?
- 최종 사용자에게 보여줄 결과는 충분히 이해하기 쉬운가?
