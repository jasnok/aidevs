# 02 Policy Based Response Validation

이 실습은 Agent 응답이 운영 정책을 위반하지 않는지 검증하는 방법을 다룹니다.

## 정책 예시

| 정책 | 설명 |
| --- | --- |
| 민감 정보 금지 | API Key, 비밀번호, 개인정보 출력 금지 |
| 위험 작업 제한 | 삭제, 결제, 권한 변경 같은 작업은 확인 필요 |
| 불확실성 표시 | 확실하지 않은 정보는 단정하지 않음 |
| 내부 로그 보호 | 내부 오류 로그를 그대로 노출하지 않음 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\03_ai-security-and-guardrails
python .\02_policy-based-response-validation\01_policy-response-validator.py
```

## 확인할 것

- 정책 위반 응답을 감지하는가?
- 위반 사유를 기록하는가?
- 안전한 대체 응답을 만들 수 있는가?
