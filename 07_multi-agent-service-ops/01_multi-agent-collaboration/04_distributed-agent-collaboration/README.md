# 04 Distributed Agent Collaboration

이 실습은 여러 Agent가 각각 작업을 수행하고 결과를 통합하는 구조를 다룹니다.

## 기본 흐름

```text
요청 입력
-> 여러 Agent에게 작업 분배
-> Agent별 결과 수집
-> 결과 충돌 여부 확인
-> 최종 보고서 생성
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\04_distributed-agent-collaboration\01_distributed-agent-collaboration.py
```

## Docker Compose 연결

나중에는 Agent 역할을 별도 프로세스나 컨테이너로 분리할 수 있습니다.

```text
backend : 요청 접수
worker  : Agent 작업 처리
monitor : 결과와 상태 확인
```

## 확인할 것

- 병렬로 실행해도 되는 작업과 순서가 필요한 작업을 구분합니다.
- 결과 통합 Agent가 왜 필요한지 확인합니다.
- 결과가 서로 충돌할 때 어떤 기준으로 최종 결정을 내릴지 정합니다.
