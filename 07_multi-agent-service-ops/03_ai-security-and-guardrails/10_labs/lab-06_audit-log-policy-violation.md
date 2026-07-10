# Lab 06. Audit Log Policy Violation

## 목표

정책 위반과 권한 위반 이벤트를 감사 로그로 추적하는 구조를 설계합니다.

## 감사 로그 필드 예시

| 필드 | 설명 |
| --- | --- |
| request_id | 요청 ID |
| agent_name | 실행 Agent |
| event_type | 정책 위반, 권한 위반, 입력 차단 등 |
| policy_name | 적용된 정책 |
| action | allow, block, mask, fallback |
| reason | 판단 이유 |
| timestamp | 발생 시간 |

## 작성할 내용

- 정책 위반 시나리오 2개
- 권한 위반 시나리오 1개
- 로그 필드 설계
- monitor 대시보드에 표시할 항목
