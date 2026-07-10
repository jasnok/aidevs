# Lab 01. Docker Build And Run

## 목표

FastAPI backend 서비스를 Docker image로 만들고 container로 실행합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## 작성할 내용

- build 성공 여부
- container 실행 여부
- `/health` 응답 결과
- Dockerfile에서 이해한 부분
