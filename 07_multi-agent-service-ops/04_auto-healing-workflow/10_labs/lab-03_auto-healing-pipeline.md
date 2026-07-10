# Lab 03. Auto Healing Pipeline

## 목표

장애 감지부터 복구 결과 기록까지의 전체 파이프라인을 설계합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\03_recovery-pipeline\01_auto-healing-pipeline.py
```

## 작성할 내용

```text
detect_failure
-> classify_failure
-> choose_recovery_action
-> run_recovery
-> validate_recovery
-> write_event_log
```

각 단계의 입력값과 출력값을 정리합니다.
