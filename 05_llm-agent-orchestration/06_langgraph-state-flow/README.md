# 06 LangGraph State Flow

이 단원에서는 Agent 실행 흐름을 LangGraph의 State, Node, Edge 구조로 설계하는 방법을 학습합니다.

앞 단원에서 Prompt, Tool Calling, RAG, Memory를 각각 배웠다면, 이 단원에서는 그 요소들을 하나의 상태 기반 실행 흐름으로 연결합니다.

## 학습 목표

- LangGraph의 State, Node, Edge 개념을 이해합니다.
- 여러 단계의 상태 업데이트 흐름을 구현합니다.
- 조건 분기, Retry, Self-Reflection 구조를 설계합니다.
- Tool Node와 RAG Node를 Agent 흐름에 연결합니다.
- Session Memory와 Vector Memory를 함께 사용하는 Hybrid Memory 흐름을 확인합니다.
- Planning, Tracing, Evaluation 관점에서 Agent 실행 결과를 점검합니다.

## 폴더 구성

```text
06_langgraph-state-flow
├─ .env.example
├─ README.md
├─ 00_references
│  └─ README.md
├─ 01_langgraph-basic-state-node-edge
│  ├─ README.md
│  ├─ 01_basic-state-graph.py
│  └─ 02_multi-step-state-update.py
├─ 02_conditional-routing
│  ├─ README.md
│  ├─ 01_conditional-route-basic.py
│  └─ 02_retry-and-reflection-flow.py
├─ 03_tool-and-rag-node-flow
│  ├─ README.md
│  ├─ 01_tool-node-style-flow.py
│  ├─ 02_mock-rag-node-flow.py
│  ├─ 03_llm-answer-node.py
│  └─ 04_hybrid-memory-flow.py
├─ 04_debugging-with-langsmith
│  ├─ README.md
│  ├─ 01_tracing-env-check.py
│  └─ 02_planning-tracing-evaluation.py
├─ 10_labs
└─ 20_assignments
```

## 실습 환경 준비

```powershell
cd C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install langgraph langchain langchain-openai langchain-core openai python-dotenv
Copy-Item .env.example .env
```

`.env` 파일은 이 단원 폴더 안의 파일을 사용합니다. LangSmith는 선택 실습이므로 처음에는 `LANGSMITH_TRACING=false`로 두고 진행해도 됩니다.

## 실행 순서

```powershell
python .\01_langgraph-basic-state-node-edge\01_basic-state-graph.py
python .\01_langgraph-basic-state-node-edge\02_multi-step-state-update.py
python .\02_conditional-routing\01_conditional-route-basic.py
python .\02_conditional-routing\02_retry-and-reflection-flow.py
python .\03_tool-and-rag-node-flow\01_tool-node-style-flow.py
python .\03_tool-and-rag-node-flow\02_mock-rag-node-flow.py
python .\03_tool-and-rag-node-flow\03_llm-answer-node.py
python .\03_tool-and-rag-node-flow\04_hybrid-memory-flow.py
python .\04_debugging-with-langsmith\01_tracing-env-check.py
python .\04_debugging-with-langsmith\02_planning-tracing-evaluation.py
```

## 단원별 핵심 질문

| 폴더 | 핵심 질문 |
| --- | --- |
| `01_langgraph-basic-state-node-edge` | State에는 어떤 정보를 넣어야 하며 Node는 무엇을 반환해야 하는가? |
| `02_conditional-routing` | 조건 분기와 Retry는 Agent 안정성에 어떤 도움을 주는가? |
| `03_tool-and-rag-node-flow` | Tool, RAG, Memory 결과를 하나의 State에 어떻게 통합하는가? |
| `04_debugging-with-langsmith` | 실행 추적은 Agent 디버깅과 품질 개선에 어떤 도움을 주는가? |

## LangChain과 LangGraph 사용 기준

LangGraph는 Agent의 실행 흐름을 명확히 표현하기 위한 도구입니다. 단순한 LLM 호출은 직접 API로도 충분하지만, 분기, 재시도, 도구 호출, 메모리, 평가 흐름이 함께 들어가면 LangGraph를 사용하는 편이 구조를 설명하기 쉽습니다.

LangChain은 필수라기보다 LangGraph와 함께 쓰기 쉬운 보조 도구입니다. 이 과정에서는 LangChain을 깊게 다루기보다 Prompt, Tool, LLM 호출을 연결하는 데 필요한 수준으로 사용합니다.

## 산출물 기준

- State 구조 정의
- Node별 입력과 출력 설명
- 조건 분기 기준
- Retry와 Self-Reflection 적용 위치
- 실행 추적 또는 평가 결과 기록
