# 03 Supervisor Router Workflow

이 실습은 Supervisor 또는 Router가 요청 유형에 따라 담당 Agent를 선택하는 구조를 다룹니다.

## 기본 흐름

```text
요청 입력
-> 요청 유형 분석
-> 담당 Agent 선택
-> Agent 실행
-> 결과 수집
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\03_supervisor-router-workflow\01_supervisor-router-workflow.py
```

## 확인할 것

- 요청 유형과 담당 Agent가 어떻게 매핑되는지 확인합니다.
- 새로운 요청 유형이 추가되면 Router 규칙이 어떻게 바뀌는지 생각합니다.
- 잘못된 Agent가 선택되었을 때 fallback이 필요한지 확인합니다.
