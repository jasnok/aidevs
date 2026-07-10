# 보안/가드레일 정책 문서 샘플

## 입력 검증

| 위험 입력 | 처리 |
| --- | --- |
| Prompt Injection | 차단 또는 재질문 |
| 비밀값 요청 | 거부 |
| 권한 없는 Tool 실행 요청 | 차단 |
| 운영 명령 직접 실행 요청 | 승인 절차 필요 |

## Agent 권한

| Agent | 허용 Tool | 금지 Tool |
| --- | --- | --- |
| Supervisor Agent | route, summarize | restart_service |
| Ops Agent | health_check, read_logs | delete_resource |
| Security Agent | validate_policy, audit_log | restart_service |
| Recovery Agent | retry, restart_request, fallback | read_secret |

## 감사 로그

정책 위반 또는 권한 차단은 다음 필드로 기록합니다.

| 필드 | 설명 |
| --- | --- |
| `request_id` | 요청 ID |
| `agent` | 판단한 Agent |
| `policy` | 적용한 정책 |
| `decision` | allow/block/escalate |
| `reason` | 판단 이유 |
