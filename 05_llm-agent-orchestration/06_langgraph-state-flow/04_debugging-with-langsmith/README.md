# 04 Debugging with LangSmith

이 폴더에서는 Agent 실행 흐름을 추적하고 평가하는 관점을 학습합니다.

## 핵심 개념

- Tracing은 Agent가 어떤 순서로 실행되었는지 기록합니다.
- Planning은 실행 전에 작업 순서를 정하는 과정입니다.
- Evaluation은 결과가 기준을 만족하는지 평가하는 과정입니다.
- LangSmith는 LangChain/LangGraph 실행 추적에 사용할 수 있는 선택 도구입니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_tracing-env-check.py` | LangSmith 환경 변수 설정 상태를 확인합니다. |
| `02_planning-tracing-evaluation.py` | 계획, 실행 기록, 평가 흐름을 간단히 실습합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow
.\.venv\Scripts\Activate.ps1
python .\04_debugging-with-langsmith\01_tracing-env-check.py
python .\04_debugging-with-langsmith\02_planning-tracing-evaluation.py
```

## 확인 질문

- Agent가 실패했을 때 어느 Node에서 문제가 생겼는지 어떻게 찾을 수 있는가?
- 평가 기준이 없으면 개선이 어려운 이유는 무엇인가?
- LangSmith를 꼭 써야 하는 경우와 로컬 로그로 충분한 경우는 어떻게 구분할 수 있는가?
