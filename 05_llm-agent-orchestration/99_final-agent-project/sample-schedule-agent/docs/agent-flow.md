# Agent Flow

이 문서는 샘플 일정 조정 Agent의 실행 흐름을 설명합니다.

## 흐름 요약

```text
사용자 요청
-> 요청 분석
-> 참석자 일정 조회 Tool
-> 가능한 시간 찾기 Tool
-> 일정 제안 메시지 생성 Tool
-> 최종 응답
```

## State 예시

| 필드 | 의미 |
| --- | --- |
| `user_request` | 사용자의 원본 요청 |
| `participants` | 일정 조정 대상자 |
| `duration_minutes` | 회의 시간 |
| `available_slots` | 가능한 시간 후보 |
| `selected_slot` | 선택된 시간 |
| `final_message` | 사용자에게 보여줄 최종 메시지 |

## Node 역할

| Node | 역할 |
| --- | --- |
| `parse_request` | 요청에서 참석자와 조건을 추출 |
| `check_calendar` | Mock 일정 데이터를 조회 |
| `find_slot` | 가능한 시간 후보를 계산 |
| `draft_message` | 최종 제안 메시지를 생성 |

## 수업 질문

- State에 꼭 필요한 필드는 무엇인가요?
- Tool 결과는 어느 Node에서 검증해야 할까요?
- 실패 상황이 생기면 어떤 Fallback이 필요할까요?

