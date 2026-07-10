# 03 Prompt, LangChain, Tool, RAG, LangGraph Map

이 과정의 용어들은 서로 연결되어 있습니다.

## 한 줄 요약

```text
Prompt는 지시문이다.
LangChain은 실행 단계를 연결한다.
Tool은 외부 기능이다.
RAG는 필요한 지식을 검색한다.
LangGraph는 전체 흐름을 상태 그래프로 관리한다.
```

## Prompt

프롬프트는 LLM에게 전달하는 지시문입니다.

좋은 프롬프트에는 보통 다음이 들어갑니다.

- 역할
- 배경 정보
- 작업 지시
- 출력 형식
- 제한 조건
- 예시

## LangChain

LangChain은 프롬프트, 모델, 출력 파서를 연결하는 데 도움을 줍니다.

```python
chain = prompt | model | parser
```

이 구조를 이해하면 이후 RAG와 LangGraph로 넘어가기 쉽습니다.

## Tool

Tool은 LLM이 사용할 수 있는 외부 기능입니다.

예시:

- 일정 조회 함수
- 총 학습 시간 계산 함수
- 날씨 API 호출 함수
- DB 검색 함수
- 문서 검색 함수

중요한 점은 LLM이 도구를 직접 실행하지 않는다는 것입니다.

```text
LLM이 도구 호출을 요청한다.
Python 코드가 실제 도구를 실행한다.
도구 결과를 다시 LLM에게 전달한다.
```

## RAG

RAG는 문서를 검색해서 답변에 넣는 방식입니다.

```text
질문
-> 질문 embedding 생성
-> 비슷한 문서 chunk 검색
-> 검색 결과를 context로 구성
-> LLM 답변 생성
```

## LangGraph

LangGraph는 여러 단계를 상태로 관리합니다.

```text
State: 현재 작업 상태
Node: 작업 단계
Edge: 다음 단계 연결
Conditional Edge: 조건에 따라 다음 단계 선택
```

## 전체 연결 예시

```text
사용자 요청
-> Prompt로 요청 분석
-> LangChain으로 모델 호출 구조화
-> Tool로 일정 조회
-> RAG로 참고 문서 검색
-> LangGraph로 전체 흐름 제어
-> 최종 답변
```
