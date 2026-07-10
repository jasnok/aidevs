# 02 Health Check Retry Restart

이 실습은 Health Check, Retry, Restart의 차이를 학습합니다.

## 개념 비교

| 개념 | 설명 |
| --- | --- |
| Health Check | 서비스가 정상인지 확인하는 검사 |
| Retry | 같은 작업을 다시 시도 |
| Restart | 서비스 프로세스나 컨테이너를 다시 시작 |
| Fallback | 원래 경로 대신 대체 경로를 사용 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\02_health-check-retry-restart\01_health-check-retry-restart.py
```

## 중요한 순서

```text
Health Check 실패
-> 일시적 오류면 Retry
-> 서비스 자체 문제면 Restart
-> 그래도 실패하면 Fallback 또는 수동 확인
```

## 확인할 것

- 무조건 재시도하지 않는가?
- 최대 재시도 횟수가 있는가?
- 재시작이 필요한 경우와 아닌 경우를 구분하는가?
