# 03 Service Health And Runtime

이 실습은 서비스가 실행 중인지 확인하는 Health Check와 runtime 로그 확인 방법을 다룹니다.

## Health Check란?

Health Check는 서비스가 정상적으로 요청을 받을 수 있는지 확인하는 검사입니다.

```text
GET /health
```

정상 응답 예시:

```json
{"status": "ok"}
```

## 확인 명령

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
docker compose ps
docker compose logs backend
docker compose logs worker
```

## 운영 관점에서 확인할 것

- 서비스가 실행 중인가?
- health endpoint가 정상 응답하는가?
- 최근 오류 로그가 있는가?
- worker가 작업을 처리하고 있는가?
- monitor에서 상태를 볼 수 있는가?
