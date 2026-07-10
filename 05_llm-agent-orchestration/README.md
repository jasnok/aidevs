# 05_llm-agent-orchestration

단일 에이전트 추론과 AI 오케스트레이션을 학습하는 과정입니다.

이 과정에서는 OpenAI API와 로컬 Llama 호출 방식을 비교하고, 프롬프트 설계, Structured Output, Function Calling, Tool Use, MCP 개념, RAG, Memory, LangGraph 상태 흐름을 순서대로 연결합니다.

05 과정의 Docker 사용 범위는 **Docker Desktop + `docker run`** 입니다. Docker Compose, Dockerfile, AWS 배포, GitHub Actions, 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 과정 방향

앞의 `02`, `03`, `04`에서는 Supabase를 사용해 백엔드, 프론트엔드, 미니 프로젝트를 빠르게 만들었습니다. 05 과정에서는 Supabase 중심이 아니라, Agent가 직접 사용할 로컬 실행 도구를 Docker 컨테이너로 띄워 봅니다.

```text
Ollama 컨테이너      -> 선택 로컬 LLM 실습
pgvector 컨테이너    -> PostgreSQL + pgvector 기반 RAG/장기 기억 실습
Redis 컨테이너       -> 세션 메모리와 캐시 실습
```

핵심은 Docker 운영이 아니라 **LLM이 도구를 호출하고, 여러 단계를 거쳐 판단하고, 상태를 유지하며, 검색 결과와 기억을 활용하는 구조**를 이해하는 것입니다.

## 05와 07의 역할 구분

```text
05_llm-agent-orchestration
-> docker run으로 필요한 로컬 도구만 실행
-> Prompt, Tool, MCP, RAG, Memory, LangGraph 흐름 학습

07_multi-agent-service-ops
-> Dockerfile, Docker Compose, Health Check, AWS, GitHub Actions
-> 서비스 운영, 배포, 자동 복구, 모니터링 학습
```

05에서는 여러 컨테이너를 하나의 Compose 파일로 묶지 않습니다. 컨테이너를 하나씩 실행하면서 Agent 실습에 필요한 도구의 역할을 이해합니다.

## 수강생 진행 기준

- 필수: OpenAI 기본 호출, Prompt 설계, Structured Output, Function Calling, Tool Use, RAG/Memory, LangGraph 상태 흐름을 실습합니다.
- 기본 유지: Ollama Docker, MCP 개념, LangSmith 개념은 과정 안에 포함합니다.
- 선택 심화: 간단한 MCP 서버, LangSmith tracing, Ollama 모델 비교, RAGAS 도구 사용은 진도와 수업 상황에 따라 다룹니다.
- 다음 과정으로 넘어가기 전: 단일 Agent가 State, Tool, Memory, RAG 결과를 어떤 흐름으로 사용하는지 다이어그램이나 코드로 설명할 수 있어야 합니다.

## 막혔을 때 바로 보기

| 막히는 지점 | 확인 문서 |
| --- | --- |
| OpenAI API key, 비용, 호출 제한 | [Gemini/OpenAI 계정과 비용](../00_course-guide/02_setup-guides/08_gemini-openai-account-guide.md), [OpenAI 기본 호출](./01_llm-api-and-local-llm/01_openai-api-basic/README.md) |
| Docker Desktop 또는 `docker run` 오류 | [Docker Desktop 설치 가이드](../00_course-guide/02_setup-guides/14_docker-desktop-guide.md), [Docker Desktop 설치 안내](./00_references/09_docker-desktop-install-for-beginners.md) |
| pgvector 또는 Redis 연결 오류 | [SETUP.md](./SETUP.md), [공통 오류 정리](./00_references/07_common-errors-for-beginners.md) |
| LangGraph 상태 흐름 이해가 어려움 | [LangGraph state flow](./06_langgraph-state-flow/README.md), [Tool/RAG node flow](./06_langgraph-state-flow/03_tool-and-rag-node-flow/README.md) |
| 단원별 `.venv` 방식이 헷갈림 | [SETUP.md](./SETUP.md), [로컬 환경 체크리스트](./00_references/05_local-environment-checklist.md) |

## 학습 목표

- OpenAI API와 로컬 Llama 호출 방식의 차이를 설명할 수 있습니다.
- 역할(Role), 지시문(Instruction), 맥락(Context) 기반 프롬프트를 설계할 수 있습니다.
- CoT/ReAct 계열의 단계적 문제 해결 흐름을 안전한 방식으로 설계할 수 있습니다.
- JSON Schema와 Pydantic 기반 Structured Output을 만들 수 있습니다.
- Prompt Injection을 이해하고 입력 검증과 시스템 프롬프트 보안 기준을 적용할 수 있습니다.
- Function Calling과 Tool Use 흐름을 구현할 수 있습니다.
- LangChain의 ChatPromptTemplate, LCEL, `with_structured_output`을 필요한 만큼 사용할 수 있습니다.
- MCP가 외부 도구 연결을 표준화하려는 방식임을 설명할 수 있습니다.
- Embedding, PostgreSQL, pgvector, RAG, Hybrid Search, RRF의 기본 구조를 설명할 수 있습니다.
- PostgreSQL Session Memory와 Vector Memory를 구분하고 결합할 수 있습니다.
- LangGraph의 Node, Edge, State 구조로 Agent 실행 흐름을 구성할 수 있습니다.
- Self-Reflection, Retry, Fallback, Tracing 관점에서 Agent 실행을 점검할 수 있습니다.

## 과정 구조

```text
05_llm-agent-orchestration
├─ README.md
├─ SETUP.md
├─ .env.example
├─ requirements.txt
├─ 00_references
├─ 01_llm-api-and-local-llm
├─ 02_prompt-and-response-quality
├─ 03_langchain-minimal
├─ 04_function-calling-and-tool-use
├─ 05_rag-memory-and-vector-search
├─ 06_langgraph-state-flow
├─ 90_ai-assisted-agent-review-and-debugging
└─ 99_final-agent-project
```

## 권장 학습 순서

```text
00_references
-> 01_llm-api-and-local-llm
-> 02_prompt-and-response-quality
-> 03_langchain-minimal
-> 04_function-calling-and-tool-use
-> 05_rag-memory-and-vector-search
-> 06_langgraph-state-flow
-> 90_ai-assisted-agent-review-and-debugging
-> 99_final-agent-project
```

## 단원 매핑

| 교육 내용 | 주 단원 |
| --- | --- |
| OpenAI API, Ollama, 로컬 LLM 비교 | `01_llm-api-and-local-llm` |
| Role/Instruction/Context, CoT/ReAct, Prompt Injection | `02_prompt-and-response-quality` |
| ChatPromptTemplate, LCEL, Structured Output | `03_langchain-minimal` |
| Function Calling, Tool Use, LangChain Tool Binding, MCP | `04_function-calling-and-tool-use` |
| Embedding, PostgreSQL, pgvector, RAG, Memory, RRF | `05_rag-memory-and-vector-search` |
| LangGraph, Hybrid Memory, Self-Reflection, Tracing | `06_langgraph-state-flow` |
| 오류 해결, AI 코드 리뷰, 디버깅 체크리스트 | `90_ai-assisted-agent-review-and-debugging` |
| 복합 API 연계 일정 조정 Agent | `99_final-agent-project` |

## 가상환경 기준

05 과정은 단원별 `.venv` 방식을 우선 권장합니다. 단원별로 OpenAI SDK, LangChain, LangGraph, psycopg, redis, MCP 관련 패키지 사용 범위가 달라질 수 있기 때문입니다.

예를 들어 첫 단원을 시작할 때는 다음처럼 진행합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
```

전체 과정을 하나의 가상환경에서 복습하고 싶다면 최상위 `requirements.txt`를 사용할 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Docker 실행 요약

Docker Desktop을 먼저 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

Ollama는 선택 실습입니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

pgvector는 RAG와 장기 기억 실습에 사용합니다.

```powershell
docker run -d `
  --name aidev-pgvector `
  -p 5433:5432 `
  -e POSTGRES_DB=agent_db `
  -e POSTGRES_USER=agent_user `
  -e POSTGRES_PASSWORD=agent_password `
  -v aidev-pgvector-data:/var/lib/postgresql/data `
  pgvector/pgvector:pg16
```

Redis는 세션 메모리와 캐시 실습에 사용합니다.

```powershell
docker run -d `
  --name aidev-redis `
  -p 6379:6379 `
  redis:7
```
