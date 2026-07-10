# 02 Role Based Agent Design

이 실습은 Agent를 역할(Role) 기준으로 나누는 방법을 다룹니다.

## 역할 예시

| Agent | 책임 |
| --- | --- |
| Supervisor Agent | 요청을 보고 어떤 Agent가 처리할지 결정 |
| Diagnosis Agent | 장애 원인 분석 |
| Recovery Agent | 복구 전략 선택 |
| Validation Agent | 복구 결과 검증 |
| Reporter Agent | 결과 요약 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\02_role-based-agent-design\01_role-based-agent-design.py
```

## 설계 기준

- 한 Agent가 너무 많은 일을 하지 않게 나눕니다.
- Agent의 입력과 출력 형식을 명확히 합니다.
- 다음 Agent에게 넘길 Context를 미리 정합니다.
- 실패했을 때 어느 Agent부터 다시 실행할지 정합니다.
