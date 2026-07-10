# Lab 02. Health Check Retry Restart

## 목표

Health Check 결과에 따라 retry, restart, fallback 중 어떤 전략을 선택할지 정합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\02_health-check-retry-restart\01_health-check-retry-restart.py
```

## 작성할 내용

- Health Check 실패 조건
- Retry가 적합한 경우
- Restart가 적합한 경우
- Fallback이 필요한 경우
- 최대 재시도 횟수
