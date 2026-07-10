# Curriculum and Lab Review

05 과정은 LLM Agent 오케스트레이션의 핵심 개념을 실습 중심으로 확인합니다. Prompt, structured output, LangChain 최소 활용, Function Calling, Tool Use, MCP, RAG, memory, LangGraph 흐름을 점검합니다.

05 과정은 단원별 `.venv`를 우선 권장합니다.

## 교육 항목 매핑

| 교육 항목 | 확인 단원 |
| --- | --- |
| Role, Instruction, Context 기반 프롬프트 | `02_prompt-and-response-quality` |
| CoT/ReAct 기반 단계적 문제 해결 | `02_prompt-and-response-quality` |
| ChatPromptTemplate, LCEL, Structured Output | `03_langchain-minimal` |
| Function Calling, Python Tool, 외부 API Tool | `04_function-calling-and-tool-use` |
| MCP 기반 외부 도구 연결 구조 | `04_function-calling-and-tool-use` |
| Embedding, PostgreSQL, pgvector, RAG | `05_rag-memory-and-vector-search` |
| PostgreSQL Session Memory, Redis Cache | `05_rag-memory-and-vector-search` |
| LangGraph Node, Edge, State | `06_langgraph-state-flow` |
| Hybrid Memory, Self-Reflection, Tracing | `06_langgraph-state-flow` |
| 복합 API 연계 일정 조정 Agent | `99_final-agent-project` |

## 보강 기준

- LangChain은 깊게 확장하지 않고 Agent 흐름에 필요한 최소 기능만 다룹니다.
- MCP는 기본 개념과 간단한 선택 실습까지 다룹니다.
- RAGAS는 필수 구현이 아니라 RAG 평가 도구의 예시로 소개합니다.
- Docker Compose와 배포 자동화는 07 과정에서 다룹니다.
