# 01 Course Big Picture

`05_llm-agent-orchestration` 과정은 LLM 기반 에이전트를 만드는 과정입니다.

## 에이전트란 무엇인가?

이 과정에서 말하는 에이전트는 단순히 답변만 하는 챗봇이 아닙니다.

에이전트는 사용자의 요청을 이해하고, 필요한 작업을 나누고, 도구를 사용하고, 결과를 정리해 답변하는 프로그램입니다.

예를 들어 사용자가 이렇게 말합니다.

```text
Kim, Lee, Park이 모두 가능한 회의 시간을 찾아서 메시지 초안을 만들어줘.
```

단순 챗봇이라면 대충 좋은 시간대를 말할 수 있습니다.

하지만 에이전트는 다음 흐름을 가질 수 있습니다.

```text
1. 참석자 이름을 찾는다.
2. 참석자별 일정을 조회한다.
3. 공통 가능한 시간을 계산한다.
4. 가장 좋은 후보를 선택한다.
5. 회의 제안 메시지를 작성한다.
6. 최종 답변을 사용자에게 보여준다.
```

## 전체 단원 흐름

```text
01_llm-api-and-local-llm
-> OpenAI API와 로컬 Llama를 호출한다.

02_prompt-and-response-quality
-> 더 안정적인 프롬프트와 출력 구조를 만든다.

03_langchain-minimal
-> 프롬프트, 모델, 파서를 체인으로 연결한다.

04_function-calling-and-tool-use
-> LLM이 사용할 수 있는 도구를 정의하고 실행한다.

05_rag-memory-and-vector-search
-> 문서를 검색해서 답변에 활용한다.

06_langgraph-state-flow
-> 여러 단계를 상태 그래프로 연결한다.

90_ai-assisted-agent-review-and-debugging
-> 오류를 찾고 AI와 함께 디버깅하는 방법을 정리한다.

99_final-agent-project
-> 일정 조정 에이전트 프로젝트를 만든다.
```

## 초보자가 헷갈리기 쉬운 점

### LLM은 모든 것을 직접 하지 않는다

LLM은 판단과 문장 생성을 잘합니다. 하지만 실제 DB 조회, API 호출, 파일 읽기, 계산은 프로그램 코드가 합니다.

```text
LLM: 어떤 도구가 필요한지 판단
Python: 실제 도구 실행
LLM: 실행 결과를 바탕으로 답변 작성
```

### RAG는 모델을 학습시키는 것이 아니다

RAG는 모델을 새로 학습시키는 것이 아닙니다.

문서를 검색해서, 검색된 내용을 프롬프트에 넣고, 그 근거로 답변하게 만드는 방식입니다.

### LangGraph는 모델이 아니다

LangGraph는 LLM 모델이 아닙니다.

에이전트가 어떤 순서로 동작할지 관리하는 실행 흐름 도구입니다.

### Docker Compose는 07에서 다룬다

05 과정의 Docker는 로컬 도구를 실행하기 위한 `docker run` 중심입니다.

```text
Ollama -> 로컬 LLM 비교
PostgreSQL + pgvector -> RAG와 장기 기억
Redis -> 세션 메모리와 캐시
```

여러 서비스를 하나의 파일로 묶어 운영하는 Docker Compose, 배포, 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

