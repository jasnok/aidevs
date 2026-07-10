# 00 References

이 문서는 `06_langgraph-state-flow` 실습에서 반복해서 등장하는 개념을 정리합니다.

## State

State는 Agent 실행 중 공유되는 데이터입니다. 예를 들어 사용자 질문, 검색 결과, Tool 실행 결과, 오류 횟수, 최종 답변을 하나의 State에 담을 수 있습니다.

State를 잘 설계하면 각 Node가 같은 정보를 기준으로 동작하므로 흐름을 추적하기 쉽습니다.

## Node

Node는 State를 입력받아 처리하고, 변경된 State를 반환하는 실행 단위입니다. Python 함수와 비슷하지만, Agent 흐름 안에서 어떤 단계인지가 더 명확하게 드러납니다.

예를 들어 다음과 같은 Node를 만들 수 있습니다.

- 질문 분석 Node
- Tool 실행 Node
- RAG 검색 Node
- 답변 생성 Node
- 검증 Node
- 재시도 Node

## Edge

Edge는 Node와 Node를 연결하는 선입니다. 단순 연결은 항상 다음 Node로 이동하고, 조건 Edge는 State 값을 보고 다음 Node를 선택합니다.

## Conditional Routing

Conditional Routing은 조건에 따라 실행 흐름을 바꾸는 구조입니다. 예를 들어 검색 결과가 부족하면 RAG 검색을 다시 실행하고, 오류가 있으면 수정 Node로 이동할 수 있습니다.

## Retry와 Self-Reflection

Retry는 실패한 작업을 다시 시도하는 구조입니다. Self-Reflection은 Agent가 자신의 결과를 점검하고 개선 방향을 정하는 구조입니다.

두 구조 모두 무한 반복을 막기 위해 최대 시도 횟수와 종료 조건이 필요합니다.

## LangSmith

LangSmith는 LangChain/LangGraph 실행 흐름을 추적하는 선택 도구입니다. 어떤 Node가 어떤 입력을 받았고 어떤 출력을 만들었는지 확인할 수 있어 Agent 디버깅에 도움이 됩니다.

처음에는 로컬 로그만으로도 충분합니다. 이후 실행 흐름이 복잡해지면 LangSmith를 선택적으로 사용합니다.
