# 04 Security Guardrail Review

## 점검 항목

- Prompt Injection 의심 입력을 감지하는가?
- 정책 위반 응답을 차단하거나 수정하는가?
- Agent 역할별로 Tool 실행 권한이 분리되어 있는가?
- 위험한 Tool 실행 전에 승인 또는 정책 검증이 있는가?
- 정책 위반 로그가 남는가?
- 로그에 API Key, Access Key, 개인정보가 노출되지 않는가?

## Codex 질문 예시

```text
다음 Tool 권한 정책이 멀티 에이전트 환경에서 안전한지 검토해줘.
Agent 역할:
- supervisor
- ops_agent
- security_agent
- recovery_agent
Tool 목록:
...
권한 정책:
...
우회 가능한 지점이 있는지 알려줘.
```

## 수정 전 확인

보안 정책을 고치기 전에 먼저 테스트 입력을 정리합니다.

| 입력 | 기대 결과 |
| --- | --- |
| 정상 요청 | 허용 |
| Prompt Injection | 차단 |
| 권한 없는 Tool 실행 | 차단 |
| 민감 정보 요청 | 거부 |
