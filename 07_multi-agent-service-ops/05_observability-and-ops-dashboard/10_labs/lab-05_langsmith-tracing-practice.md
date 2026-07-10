# Lab 05. LangSmith Tracing Practice

## 목표

LangSmith 기반 실행 추적이 어떤 정보를 기록하는지 이해하고, Multi-Agent 실행 흐름을 trace/run/span 관점으로 정리합니다.

이 실습은 외부 LangSmith API를 호출하지 않고 Mock 데이터로 구조를 먼저 이해합니다. 실제 LangSmith 연동은 API Key, 프로젝트 설정, SDK 버전에 따라 달라질 수 있으므로 선택 실습으로 진행합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\02_tracing-and-monitoring\02_langsmith_trace_mapping.py
```

## 작성할 내용

- trace와 run의 차이
- parent_run_id가 필요한 이유
- 기록하면 안 되는 민감 정보
- 실패 run을 찾는 기준
- Auto Healing 결과와 trace를 연결하는 방법
