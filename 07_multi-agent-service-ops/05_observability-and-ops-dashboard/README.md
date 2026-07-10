# 05 Observability And Ops Dashboard

이 단원은 AI 서비스 운영 상태를 확인하기 위한 로그, 이벤트 이력, tracing, CloudWatch Logs, 운영 대시보드를 학습합니다.

Auto Healing이 동작하려면 장애를 감지하고 복구하는 것뿐 아니라, 그 과정이 기록되고 화면에서 확인되어야 합니다.

## 학습 목표

- 구조화된 이벤트 로그를 남깁니다.
- Agent 실행 흐름을 trace 단위로 추적합니다.
- LangSmith식 실행 추적 개념을 이해합니다.
- CloudWatch Logs에서 AWS 배포 서비스 로그를 확인합니다.
- Streamlit으로 운영 대시보드를 구성합니다.
- pending, running, success, failed 같은 실행 상태를 관리합니다.
- Auto Healing 결과를 운영 화면에서 확인합니다.

## 폴더 구조

```text
05_observability-and-ops-dashboard
├─ 01_logging-and-event-history
├─ 02_tracing-and-monitoring
├─ 03_ops-dashboard-streamlit
├─ 04_execution-status-management
├─ 05_cloudwatch-log-review
├─ 10_labs
└─ 20_assignments
```

## 실행 예시

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\01_logging-and-event-history\01_event-history-logger.py
python .\02_tracing-and-monitoring\01_trace-agent-execution.py
python .\02_tracing-and-monitoring\02_langsmith_trace_mapping.py
streamlit run .\03_ops-dashboard-streamlit\01_ops-dashboard.py --server.port 8803
python .\04_execution-status-management\01_execution-status-manager.py
```

CloudWatch 확인은 AWS 배포 후 진행합니다.

```text
05_cloudwatch-log-review/README.md
```

## 관측성 기본 구조

```text
요청 발생
-> request_id 생성
-> Agent 실행
-> Tool 호출
-> event log 기록
-> trace 기록
-> CloudWatch Logs 확인
-> dashboard 표시
```

## 확인할 지표

- 요청 수
- 성공/실패 수
- 실패 유형
- 평균 처리 시간
- 재시도 횟수
- 최근 이벤트
- 복구 성공 여부
- App Runner 배포 로그
- CloudWatch Log Group 이름

## LangSmith 위치

LangSmith는 Agent 실행 추적을 돕는 도구입니다. 이 단원에서는 먼저 Mock trace와 로컬 로그로 구조를 이해하고, 실제 LangSmith 연동은 확장 실습으로 다룹니다.
