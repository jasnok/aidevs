# 04. Docker Compose And Service Ops

Docker Compose는 여러 컨테이너 서비스를 하나의 파일로 함께 실행하는 도구입니다.

07 과정에서는 Compose를 서비스 운영 구조를 이해하는 핵심 도구로 사용합니다.

## Docker와 Docker Compose 차이

```text
Docker:
- 컨테이너 하나를 build/run

Docker Compose:
- 여러 컨테이너를 하나의 서비스 묶음으로 실행
```

## 기본 명령어

```powershell
docker compose config
docker compose up --build
docker compose up --build -d
docker compose ps
docker compose logs backend
docker compose logs -f worker
docker compose down
```

## 07 과정의 Compose 서비스

```text
backend  : FastAPI API 서버
frontend : Streamlit 화면
worker   : 백그라운드 작업 처리
monitor  : 운영 상태 대시보드
```

## 실행 순서

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 운영 관점에서 확인할 것

- 컨테이너가 모두 실행 중인가?
- backend `/health`가 정상 응답하는가?
- worker 로그에 작업 처리 이력이 남는가?
- monitor 화면에서 상태를 볼 수 있는가?
- 종료 시 `docker compose down`을 실행했는가?
