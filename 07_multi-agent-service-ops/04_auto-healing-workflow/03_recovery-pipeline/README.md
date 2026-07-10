# 03 Recovery Pipeline

이 실습은 Auto Healing 복구 파이프라인을 단계별로 설계합니다.

## 파이프라인 예시

```text
detect_failure
-> classify_failure
-> choose_recovery_action
-> run_recovery
-> validate_recovery
-> write_event_log
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\03_recovery-pipeline\01_auto-healing-pipeline.py
```

## 운영 관점

각 단계는 로그로 남깁니다.

- 어떤 서비스에 문제가 발생했는가?
- 어떤 장애 유형으로 분류했는가?
- 어떤 복구 전략을 선택했는가?
- 복구가 성공했는가?
- 추가 확인이 필요한가?
