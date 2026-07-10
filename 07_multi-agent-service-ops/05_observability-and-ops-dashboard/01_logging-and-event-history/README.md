# 01 Logging And Event History

이 실습은 서비스 실행 이벤트를 구조화해서 기록하는 방법을 다룹니다.

## 좋은 로그에 포함할 정보

| 필드 | 설명 |
| --- | --- |
| request_id | 요청 ID |
| service | backend, worker, monitor 등 |
| agent | 실행 Agent |
| event_type | started, tool_called, failed, recovered 등 |
| message | 사람이 읽을 수 있는 설명 |
| timestamp | 발생 시간 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\01_logging-and-event-history\01_event-history-logger.py
```

## 확인할 것

- 이벤트가 구조화되어 있는가?
- request_id로 관련 로그를 묶을 수 있는가?
- 실패와 복구 이벤트가 구분되는가?
