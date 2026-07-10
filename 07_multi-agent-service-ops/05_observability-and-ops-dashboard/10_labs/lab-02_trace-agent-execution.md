# Lab 02. Trace Agent Execution

## 목표

하나의 요청이 여러 Agent 단계를 거치는 흐름을 trace로 정리합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\02_tracing-and-monitoring\01_trace-agent-execution.py
```

## 작성할 내용

- trace_id
- span 목록
- 각 span의 시작/종료 시간
- 실패한 단계
- 오래 걸린 단계
