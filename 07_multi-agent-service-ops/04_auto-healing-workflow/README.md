# 04 Auto Healing Workflow

이 단원은 AI 서비스 운영 중 발생할 수 있는 장애를 감지하고, 가능한 경우 자동으로 복구하는 Auto Healing 흐름을 학습합니다.

## 학습 목표

- 장애 유형을 분류합니다.
- Health Check, Retry, Restart, Fallback의 차이를 이해합니다.
- 복구 파이프라인을 단계별로 설계합니다.
- 복구 결과를 검증합니다.
- 복구 과정과 결과를 로그로 남깁니다.

## 폴더 구조

```text
04_auto-healing-workflow
├─ 01_failure-scenarios
├─ 02_health-check-retry-restart
├─ 03_recovery-pipeline
├─ 04_recovery-result-validation
├─ 10_labs
└─ 20_assignments
```

## 기본 흐름

```text
장애 감지
-> 장애 유형 분류
-> 복구 전략 선택
-> retry/restart/fallback 실행
-> 복구 결과 검증
-> 이벤트 로그 기록
```

## 실행 예시

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\01_failure-scenarios\01_failure-scenario-classifier.py
python .\02_health-check-retry-restart\01_health-check-retry-restart.py
python .\03_recovery-pipeline\01_auto-healing-pipeline.py
python .\04_recovery-result-validation\01_recovery-result-validation.py
```

## 운영 기준

- 재시도 횟수는 반드시 제한합니다.
- 복구 전후 상태를 비교합니다.
- 자동 복구가 실패하면 사람이 확인할 수 있게 상태를 남깁니다.
- 복구 성공 여부는 느낌이 아니라 health check와 결과 검증으로 판단합니다.
