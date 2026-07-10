# 02 Docker Compose Multi Service

이 실습은 backend, frontend, worker, monitor를 Docker Compose로 함께 실행합니다.

## 서비스 구성

| 서비스 | 역할 |
| --- | --- |
| backend | FastAPI API 서버 |
| frontend | Streamlit 사용자 화면 |
| worker | 백그라운드 Agent 작업 |
| monitor | 운영 상태 확인 대시보드 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인 URL

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

## 자주 쓰는 명령

```powershell
docker compose ps
docker compose logs backend
docker compose logs -f worker
docker compose down
```

## 확인할 것

- `docker compose config`가 성공하는가?
- 네 서비스가 모두 실행되는가?
- backend health check가 정상인가?
- worker 로그가 출력되는가?
- monitor 화면에서 이벤트를 확인할 수 있는가?
