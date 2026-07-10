# Team Template

이 폴더는 최종 Agent 미니 프로젝트를 시작할 때 사용하는 템플릿입니다.

샘플 프로젝트를 그대로 복사하기보다, 해결할 문제에 맞게 State, Tool, Graph 흐름을 다시 설계하는 것이 목표입니다.

## 구성

```text
team-template
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

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\99_final-agent-project\team-template
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\backend\requirements.txt
python .\backend\graph.py
streamlit run .\frontend\app.py --server.port 8602
```

## 프로젝트 진행 순서

1. 해결할 문제를 정의합니다.
2. Agent가 필요한 이유를 설명합니다.
3. State 필드를 설계합니다.
4. Tool 목록을 작성합니다.
5. Node와 Edge 흐름을 그립니다.
6. Retry, Fallback, Self-Reflection 전략을 정합니다.
7. CLI에서 먼저 실행합니다.
8. Streamlit 화면으로 연결합니다.
9. 테스트 체크리스트를 작성합니다.
10. 발표 자료를 정리합니다.
