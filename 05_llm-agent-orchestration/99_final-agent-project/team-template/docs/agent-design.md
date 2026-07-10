# Agent Design

최종 Agent 구조를 정리하는 문서입니다.

## State 설계

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `messages` | list | 대화 메시지 |
| `required_tools` | list[str] | 필요하다고 판단한 Tool 목록 |
| `tools_called` | list[str] | 실제 호출한 Tool 목록 |
| `tool_results` | dict | Tool 실행 결과 |
| `error_count` | int | 오류 또는 재시도 횟수 |
| `memory_summary` | str | 이전 대화 요약 |
| `final_answer` | str | 최종 응답 |

## Node 설계

| Node | 역할 |
| --- | --- |
| `analyze_request` | 사용자 의도 분석 |
| `select_tool` | 필요한 Tool 선택 |
| `call_tool` | Tool 실행 |
| `validate_result` | Tool 결과 검증 |
| `reflect_or_retry` | 오류 시 수정 전략 선택 |
| `final_answer` | 최종 응답 생성 |

## Edge 설계

```text
start
-> analyze_request
-> select_tool
-> call_tool
-> validate_result
-> final_answer
```

오류가 있으면 다음 흐름을 추가합니다.

```text
validate_result
-> reflect_or_retry
-> select_tool
```

## Fallback 전략

| 오류 유형 | 처리 |
| --- | --- |
| Tool 선택 오류 | 다시 Tool 선택 |
| Tool 실행 실패 | 대체 Tool 또는 안내 메시지 |
| 정보 부족 | 사용자에게 추가 질문 |
| 반복 실패 | 안전한 최종 안내 |

