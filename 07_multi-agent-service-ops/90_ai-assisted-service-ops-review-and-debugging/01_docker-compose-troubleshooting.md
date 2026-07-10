# 01 Docker Compose Troubleshooting

## 먼저 실행할 명령

```powershell
docker --version
docker compose version
docker ps
docker compose config
docker compose ps
docker compose logs backend
docker compose logs worker
```

## 자주 보는 오류

| 증상 | 확인할 것 |
| --- | --- |
| `docker` 명령 없음 | Docker Desktop 설치와 실행 여부 |
| `docker compose config` 실패 | YAML 들여쓰기, `.env` 파일 존재 여부 |
| port already allocated | 같은 포트를 사용하는 컨테이너 또는 로컬 서버 |
| backend health 실패 | 컨테이너 포트, FastAPI 실행 명령, `/health` endpoint |
| frontend가 backend를 못 찾음 | Compose service name, `API_BASE_URL` |

## Codex 질문 예시

```text
다음 docker compose logs backend 출력에서 backend가 시작하지 못하는 원인을 찾아줘.
실행 위치: C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
실행 명령: docker compose up --build
기대 결과: backend /health가 200 응답
실제 로그:
...
```
