# 00_references

이 폴더는 `05_llm-agent-orchestration` 과정을 시작하기 전에 읽는 초보자용 참고 자료입니다.

이 과정은 OpenAI API, 로컬 Llama, Prompt Engineering, LangChain 최소 활용, Function Calling, Tool Use, MCP, RAG, PostgreSQL/pgvector, Redis, LangGraph를 다룹니다. 이름만 보면 어렵게 느껴질 수 있지만, 전체 흐름은 하나입니다.

```text
LLM에게 질문한다
-> 더 좋은 프롬프트를 만든다
-> 프롬프트와 모델 호출을 체인으로 정리한다
-> 필요한 도구를 호출하게 만든다
-> 도구 연결 표준인 MCP를 맛본다
-> 필요한 문서를 검색해서 답변하게 만든다
-> 짧은 기억과 장기 기억을 나누어 저장한다
-> 이 전체 흐름을 상태 그래프로 관리한다
-> 미니 프로젝트로 완성한다
```

## 참고 자료 목록

```text
00_references
├─ README.md
├─ 01_course-big-picture.md
├─ 02_llm-api-and-local-llama.md
├─ 03_prompt-langchain-tool-rag-langgraph-map.md
├─ 04_openai-api-key-and-cost-safety.md
├─ 05_local-environment-checklist.md
├─ 06_docker-ollama-pgvector-overview.md
├─ 07_common-errors-for-beginners.md
├─ 08_final-project-roadmap.md
├─ 09_docker-desktop-install-for-beginners.md
└─ 10_curriculum-and-lab-review.md
```

## 읽는 순서

처음에는 아래 순서대로 읽는 것을 권장합니다.

1. `01_course-big-picture.md`
2. `02_llm-api-and-local-llama.md`
3. `03_prompt-langchain-tool-rag-langgraph-map.md`
4. `04_openai-api-key-and-cost-safety.md`
5. `09_docker-desktop-install-for-beginners.md`
6. `05_local-environment-checklist.md`
7. `06_docker-ollama-pgvector-overview.md`
8. `07_common-errors-for-beginners.md`
9. `08_final-project-roadmap.md`
10. `10_curriculum-and-lab-review.md`

## 이 과정에서 가장 중요한 관점

이 과정은 “AI가 코드를 대신 짜준다”가 핵심이 아닙니다.

핵심은 다음입니다.

```text
AI 서비스를 만들 때 필요한 판단 흐름을 직접 설계한다.
```

이 과정에서는 LLM을 단순 챗봇으로 쓰는 것을 넘어, 다음 흐름을 직접 구현합니다.

- 사용자의 요청을 분석한다.
- 필요한 도구를 선택한다.
- 외부 데이터나 문서를 검색한다.
- 세션 기억과 장기 기억을 구분한다.
- 검색 결과를 근거로 답변한다.
- 여러 단계를 상태로 관리한다.
- 최종적으로 하나의 에이전트 서비스를 만든다.

