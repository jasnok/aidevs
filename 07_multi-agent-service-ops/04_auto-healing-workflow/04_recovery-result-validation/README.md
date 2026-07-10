# 04 Recovery Result Validation

이 실습은 복구 조치 후 결과를 검증하는 방법을 다룹니다.

복구 명령을 보냈다고 해서 복구가 완료된 것은 아닙니다. 반드시 복구 후 상태를 확인해야 합니다.

## 검증 기준

- `/health`가 정상 응답하는가?
- 오류 로그가 더 이상 반복되지 않는가?
- 사용자 요청을 다시 처리할 수 있는가?
- worker가 작업을 정상 처리하는가?
- 수동 확인이 필요한 상태인가?

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\04_auto-healing-workflow
python .\04_recovery-result-validation\01_recovery-result-validation.py
```

## 확인할 것

- 복구 전 상태와 복구 후 상태를 비교합니다.
- 검증 실패 시 다음 행동을 정합니다.
- 검증 결과를 로그로 남깁니다.
