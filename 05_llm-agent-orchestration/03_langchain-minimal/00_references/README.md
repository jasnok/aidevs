# 00_references

이 문서는 `03_langchain-minimal` 단원을 진행할 때 함께 보는 개념 정리입니다.

## LangChain을 배우는 이유

LangChain은 LLM API를 대신 이해해 주는 마법 도구가 아닙니다.

이 과정에서는 다음 반복 작업을 구조화하기 위해 사용합니다.

```text
프롬프트 만들기
-> 모델 호출
-> 출력 문자열 꺼내기
-> 필요하면 구조화된 객체로 검증
-> 긴 문서를 작은 조각으로 나누기
```

작은 예제에서는 OpenAI SDK를 직접 호출하는 방식이 더 단순합니다. 하지만 프롬프트, 모델, 파서, 문서 처리가 반복되면 LangChain의 `PromptTemplate`, `Runnable`, `OutputParser`가 코드를 정리하는 데 도움이 됩니다.

## PromptTemplate

PromptTemplate은 반복되는 프롬프트 문장에 값만 바꿔 넣는 도구입니다.

```text
{level} 학습자를 위해 {topic} 개념을 설명해줘.
```

이런 템플릿을 사용하면 같은 형식의 요청을 여러 주제에 반복해서 적용할 수 있습니다.

## ChatPromptTemplate

ChatPromptTemplate은 `system`, `human` 같은 역할 기반 메시지를 구성할 때 사용합니다.

02 단원에서 배운 Role, Instruction, Context 구조를 코드로 재사용하기 쉽게 만들어 줍니다.

## Runnable과 Chain

Runnable은 입력을 받아 처리하고 출력을 만드는 실행 단위입니다.

여러 Runnable을 `|` 연산자로 연결하면 다음처럼 데이터 흐름이 생깁니다.

```text
PromptTemplate -> Model -> OutputParser
```

## Document와 Text Splitter

RAG를 하려면 문서를 한 번에 통째로 넣기보다 작은 조각으로 나누어야 합니다.

```text
문서 읽기
-> Document 객체 만들기
-> chunk로 분할
-> embedding
-> vector DB 저장
-> 검색
```

이 단원에서는 RAG 전체를 완성하기보다, 문서를 읽고 나누는 전처리 감각을 먼저 익힙니다.

## 다음 단원과의 연결

```text
04_function-calling-and-tool-use
-> LangChain에서 본 Chain 흐름을 실제 Tool 호출 흐름으로 확장합니다.

05_rag-memory-and-vector-search
-> 문서 chunk를 embedding하고 pgvector에 저장합니다.

06_langgraph-state-flow
-> Chain보다 더 복잡한 Agent 상태 흐름을 그래프로 관리합니다.
```
