# Sample Auto Healing Agent

이 폴더는 06 미니 프로젝트의 완성 샘플입니다.

Docker Compose로 backend, frontend, worker, monitor를 함께 실행하고, Auto Healing 이벤트가 어떻게 기록되는지 확인합니다.

## 서비스 구성

| 서비스 | 역할 |
| --- | --- |
| backend | FastAPI API 서버, health check와 이벤트 API 제공 |
| frontend | Streamlit 사용자 화면 |
| worker | Auto Healing 작업 실행 |
| monitor | 운영 상태와 이벤트 확인 화면 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\sample-auto-healing-agent
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인 주소

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

## 확인할 것

- backend `/health`가 정상 응답하는가?
- frontend에서 Auto Healing 요청을 보낼 수 있는가?
- worker 로그에 작업 처리 이력이 남는가?
- monitor에서 이벤트 상태가 보이는가?

## 종료

```powershell
docker compose down
```
