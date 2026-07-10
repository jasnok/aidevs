# 02 Tracing And Monitoring

이 실습은 하나의 요청이 여러 Agent와 Tool 단계를 거쳐 실행되는 흐름을 trace로 추적하는 방법을 다룹니다.

## Log와 Trace 차이

| 구분 | 설명 |
| --- | --- |
| Log | 개별 사건 기록 |
| Trace | 하나의 요청이 여러 단계를 지나간 전체 경로 |
| Monitoring | 현재 서비스 상태와 지표 관찰 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\02_tracing-and-monitoring\01_trace-agent-execution.py
python .\02_tracing-and-monitoring\02_langsmith_trace_mapping.py
```

## 확인할 것

- 하나의 요청에 여러 span이 연결되는가?
- 어떤 Agent 단계가 오래 걸리는지 확인할 수 있는가?
- 실패한 단계가 trace에서 보이는가?
- LangSmith식 trace/run/span 개념과 연결되는가?
