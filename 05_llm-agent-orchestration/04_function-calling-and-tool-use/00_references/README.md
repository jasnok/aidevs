# 00_references

이 문서는 `04_function-calling-and-tool-use` 단원을 진행할 때 함께 보는 개념 정리입니다.

## Function Calling이 필요한 이유

LLM은 문장을 잘 만들지만, 모든 작업을 직접 처리하는 도구는 아닙니다.

다음 작업은 Python 함수나 외부 시스템에 맡기는 것이 더 안전합니다.

- 계산
- 데이터 조회
- 외부 API 호출
- 파일 또는 DB 처리
- 검색
- 일정, 로그, 사용자 정보 조회

Function Calling은 LLM이 “어떤 함수를 호출해야 하는지”를 판단하고, 실제 실행은 애플리케이션 코드가 담당하도록 나누는 구조입니다.

## Tool 설계 기준

좋은 Tool은 다음 기준을 만족해야 합니다.

```text
이름이 명확한가?
입력값이 명확한가?
출력값이 일정한가?
실패했을 때 오류 메시지가 있는가?
LLM이 호출해도 되는 작업인가?
```

예:

```text
Tool 이름: get_learning_logs
입력: learner 이름
출력: 학습 로그 목록
실패: 해당 학습자가 없으면 빈 목록 또는 오류 메시지
```

## Tool 호출 흐름

```text
1. 사용자 요청 입력
2. LLM이 사용할 Tool과 인자 결정
3. Python 코드가 Tool 실행
4. Tool 실행 결과를 LLM에 다시 전달
5. LLM이 최종 답변 작성
```

이 구조를 이해하면 이후 Multi-Agent, LangGraph, Auto Healing 흐름도 더 쉽게 이해할 수 있습니다.

## Mock Tool을 먼저 쓰는 이유

실제 외부 API는 네트워크 오류, 인증, 사용량 제한, 응답 형식 변경 같은 변수가 많습니다.

그래서 처음에는 Mock 데이터로 Tool 구조를 먼저 익힙니다.

```text
Mock Tool
-> 네트워크 없이 구조 이해

HTTP API Tool
-> 실제 외부 시스템과 연결
```

## Multi-Tool Orchestration

Tool이 하나일 때는 호출 흐름이 단순합니다.

하지만 Tool이 여러 개가 되면 다음 판단이 필요합니다.

- 어떤 Tool을 먼저 호출할 것인가?
- Tool 결과가 부족하면 다음 Tool을 호출할 것인가?
- Tool 결과가 서로 충돌하면 어떻게 처리할 것인가?
- 최종 응답에는 어떤 결과를 포함할 것인가?

이 판단 흐름을 설계하는 것이 오케스트레이션입니다.

## MCP와의 관계

Function Calling은 애플리케이션 코드 안에서 함수 호출을 모델과 연결하는 방식입니다.

MCP는 모델이 외부 도구와 데이터 소스에 연결되는 방식을 더 표준화하려는 개념입니다.

05 과정에서는 MCP를 Function Calling, Tool Use와 비교하고, 간단한 선택 실습 수준으로 다룹니다.

## 다음 단원과의 연결

```text
05_rag-memory-and-vector-search
-> 검색 Tool이 참조할 문서와 벡터 DB를 준비합니다.

06_langgraph-state-flow
-> Tool 호출, 조건 분기, 재시도 흐름을 StateGraph로 관리합니다.

99_final-agent-project
-> 일정 조정 Agent에서 Tool, Memory, Graph 흐름을 통합합니다.
```
