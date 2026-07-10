# Lab 02. Docker Compose Up

## 목표

Docker Compose로 backend, frontend, worker, monitor를 함께 실행합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인

```powershell
docker compose ps
docker compose logs backend
docker compose logs worker
```

## 작성할 내용

- 실행된 서비스 목록
- 서비스별 포트
- backend health 결과
- worker 로그 확인 결과
- monitor 화면 확인 결과
