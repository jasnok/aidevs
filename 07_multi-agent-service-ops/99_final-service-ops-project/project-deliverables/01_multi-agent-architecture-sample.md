# Multi-Agent 협업 구조 설계서 샘플

## 프로젝트 개요

| 항목 | 내용 |
| --- | --- |
| 프로젝트명 | Auto Healing Agent Service |
| 목표 | 장애 메시지를 분석하고 적절한 복구 action을 선택해 운영 결과를 기록합니다. |
| 실행 구조 | Docker Compose 기반 backend/frontend/worker/monitor |

## Agent 역할

| Agent | 책임 |
| --- | --- |
| Supervisor Agent | 요청을 분류하고 담당 Agent를 선택합니다. |
| Ops Agent | health check, 로그, 서비스 상태를 확인합니다. |
| Security Agent | 권한과 정책 위반 여부를 확인합니다. |
| Recovery Agent | retry, restart, fallback action을 결정합니다. |

## Handoff 흐름

```text
사용자 장애 요청
-> Supervisor Agent
-> Ops Agent 상태 확인
-> Security Agent 권한 확인
-> Recovery Agent 복구 action 결정
-> Supervisor Agent 결과 통합
-> monitor 기록
```

## 공유 상태 예시

| 필드 | 설명 |
| --- | --- |
| `request_id` | 실행 추적 ID |
| `failure_message` | 입력 장애 메시지 |
| `failure_type` | 분류된 장애 유형 |
| `assigned_agent` | 담당 Agent |
| `recovery_action` | retry/restart/fallback/escalate |
| `status` | pending/running/success/failed |
| `events` | 실행 이벤트 목록 |
