# Lab 03. Health Check And Logs

## 목표

서비스 상태를 `/health`와 Docker logs로 확인합니다.

## 실행

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
docker compose ps
docker compose logs backend
docker compose logs -f worker
```

## 작성할 내용

- health 응답 내용
- 실패 로그가 있다면 원인
- worker가 남긴 이벤트
- monitor에서 확인한 상태
