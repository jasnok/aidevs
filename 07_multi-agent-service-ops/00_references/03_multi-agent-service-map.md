# 03. Multi-Agent Service Map

Multi-Agent 서비스를 운영 관점으로 보면 Agent 코드만 있는 것이 아닙니다. 요청을 받는 API, 화면, 백그라운드 작업자, 모니터링 화면이 함께 필요합니다.

## 기본 서비스 구성

```text
frontend
-> backend
-> supervisor agent
-> diagnosis agent
-> recovery agent
-> validation agent
-> worker
-> logs/events
-> monitor
```

## 서비스별 역할

| 서비스 | 역할 |
| --- | --- |
| frontend | 사용자가 요청을 입력하고 결과를 확인하는 화면 |
| backend | API 요청을 받고 Agent 작업을 시작하는 서버 |
| worker | 오래 걸리는 Agent 작업, 복구 작업, 재시도를 처리 |
| monitor | 이벤트 로그, 장애 상태, 복구 결과를 확인하는 대시보드 |

## Agent별 역할 예시

| Agent | 역할 |
| --- | --- |
| Supervisor Agent | 전체 요청을 보고 어떤 Agent가 처리할지 결정 |
| Diagnosis Agent | 장애 원인과 오류 유형 분석 |
| Recovery Agent | retry, restart, fallback 중 복구 전략 선택 |
| Validation Agent | 복구 결과가 정상인지 확인 |
| Reporter Agent | 최종 결과와 로그를 사람이 이해하기 쉽게 요약 |

## 중요한 설계 기준

- Agent 간 Context 형식을 맞춥니다.
- 모든 Agent는 같은 `request_id`를 공유합니다.
- Agent 실행 결과는 로그로 남깁니다.
- 실패한 Agent만 다시 실행할 수 있도록 상태를 분리합니다.
