# Lab 04. Execution Status Management

## 목표

Agent 실행 상태 전이를 관리합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\04_execution-status-management\01_execution-status-manager.py
```

## 작성할 내용

```text
pending -> running -> success
pending -> running -> failed -> retrying -> success
pending -> running -> failed -> fallback
```

각 상태에서 기록할 로그를 정리합니다.
