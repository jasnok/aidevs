# 01 Failure Scenarios

이 실습은 서비스 장애 유형을 분류하는 방법을 다룹니다.

## 장애 유형 예시

| 장애 유형 | 설명 | 대응 예시 |
| --- | --- | --- |
| `unhealthy` | Health Check 실패 | 재시작 또는 점검 |
| `timeout` | 응답 지연 | retry 또는 timeout 조정 |
| `api_error` | 외부 API 5xx | 재시도 또는 fallback |
| `rate_limit` | 호출량 초과 | 대기 후 재시도 |
| `permission_error` | 권한 부족 | Secret/IAM/env 확인 |
| `unknown` | 원인 불명 | 로그 수집 후 수동 확인 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\01_failure-scenarios\01_failure-scenario-classifier.py
```

## 확인할 것

- 장애 유형이 명확히 분류되는가?
- 유형별 대응 전략이 다른가?
- 알 수 없는 장애를 어떻게 처리하는가?
