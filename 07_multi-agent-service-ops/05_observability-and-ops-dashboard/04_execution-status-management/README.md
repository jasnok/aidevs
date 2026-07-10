# 04 Execution Status Management

이 실습은 Agent 실행 상태를 관리하는 방법을 다룹니다.

## 상태 예시

```text
pending
running
success
failed
retrying
fallback
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\04_execution-status-management\01_execution-status-manager.py
```

## 필요한 이유

운영 환경에서는 사용자의 요청이나 Agent 작업이 지금 어디까지 진행되었는지 알아야 합니다.

- 작업이 아직 대기 중인가?
- 실행 중인가?
- 성공했는가?
- 실패했다면 어느 단계에서 실패했는가?
- 재시도 중인가?

## 확인할 것

- 상태 전이가 자연스러운가?
- 실패 상태가 기록되는가?
- 재시도 상태와 최종 실패 상태가 구분되는가?
