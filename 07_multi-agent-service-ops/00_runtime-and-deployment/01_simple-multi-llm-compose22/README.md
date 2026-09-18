# Simple Multi-LLM 독립 배포

이 프로젝트는 frontend와 backend를 서로 다른 AWS EC2 인스턴스에 독립적으로 배포한다.

- Frontend EC2: Streamlit frontend 컨테이너만 실행
- Backend EC2: FastAPI backend 컨테이너와 PostgreSQL, Redis 실행
- Ollama: 현재 사용하지 않음
- LLM: OpenAI 또는 Gemini API 사용

## 배포 구조

```text
사용자
  |
  v
Frontend EC2
  Streamlit :8501 (또는 Host :80)
  |
  | BACKEND_URL
  v
Backend EC2
  FastAPI :8000
  |-- PostgreSQL Host :5433 -> Container :5432
  `-- Redis      Host :6379 -> Container :6379
```

frontend와 backend는 서로 다른 Compose 프로젝트로 실행한다. 따라서 frontend에서는
`http://backend:8000`과 같은 Compose 서비스 이름을 사용할 수 없다. Backend EC2의 사설
DNS, 사설 IP 또는 공개 API 도메인을 `BACKEND_URL`로 지정해야 한다.

PostgreSQL과 Redis는 Backend EC2에서 별도로 실행하고 backend 컨테이너는
`host.docker.internal`을 통해 접근한다. `backend/compose*.yml`의 `extra_hosts`가 Linux
EC2에서 `host.docker.internal`을 host gateway로 연결한다.

## 디렉터리 구성

```text
01_simple-multi-llm-compose2/
|-- backend/
|   |-- compose.yml            # backend 로컬 빌드 및 실행
|   |-- compose.release.yml    # registry backend 이미지 배포
|   |-- .env.example
|   |-- Dockerfile
|   `-- database/init.sql
|-- frontend/
|   |-- compose.yml            # frontend 로컬 빌드 및 실행
|   |-- compose.release.yml    # registry frontend 이미지 배포
|   |-- .env.example
|   `-- Dockerfile
```

각 서비스 폴더 안의 Compose 파일만 사용한다.

- `backend/compose.yml`: backend 개발용 로컬 빌드
- `backend/compose.release.yml`: Backend EC2 배포
- `frontend/compose.yml`: frontend 개발용 로컬 빌드
- `frontend/compose.release.yml`: Frontend EC2 배포

루트의 통합 `compose.yml`, `compose.release.yml`, `compose.full-stack.yml`은 두 EC2 독립
배포 구조와 책임이 겹치므로 사용하지 않는다.

## 1. Backend EC2 준비

Backend EC2에는 다음 항목이 준비되어 있어야 한다.

- Docker와 Docker Compose
- PostgreSQL: Host 포트 `5433`
- Redis: Host 포트 `6379`
- backend 이미지를 받을 수 있는 container registry 로그인 정보

PostgreSQL과 Redis 상태를 먼저 확인한다.

```bash
docker ps
docker port <postgres-container-name>
docker port <redis-container-name>
```

예상 포트 연결은 다음과 같다.

```text
PostgreSQL  0.0.0.0:5433 -> 5432/tcp
Redis       0.0.0.0:6379 -> 6379/tcp
```

AWS Security Group에서는 `5433`과 `6379`를 인터넷에 공개하지 않는다. 두 포트는 같은
Backend EC2의 backend 컨테이너에서만 사용한다.

### 데이터베이스 초기화

최초 한 번 `backend/database/init.sql`을 PostgreSQL에 적용한다. EC2 호스트에는 `psql`을
설치하지 않고 PostgreSQL 컨테이너에 포함된 `psql`을 사용한다.

```bash
cd backend
docker exec -i simple-postgres \
  psql -U agent_user -d agent_db < database/init.sql
```

`simple-postgres`는 PostgreSQL 컨테이너 이름이다. 실제 이름이 다르면 먼저 확인해서
명령의 컨테이너 이름을 변경한다.

```bash
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}"
```

스키마 적용 결과를 확인한다.

```bash
docker exec simple-postgres \
  psql -U agent_user -d agent_db \
  -c "\dt simple_multi_llm.*"
```

초기화 스크립트는 다음 객체를 생성한다.

```text
simple_multi_llm.notes
simple_multi_llm.chat_messages
```

## 2. Backend 환경변수

Backend EC2에서 환경 파일을 만든다.

```bash
cd backend
cp .env.example .env
```

`backend/.env`를 다음과 같이 설정한다.

```ini
# GitHub Container Registry 또는 Docker Hub 이미지
BACKEND_IMAGE=ghcr.io/<owner>/simple-multi-llm-backend:<tag>
BACKEND_PORT=8000

# 같은 EC2에서 별도로 실행 중인 PostgreSQL과 Redis
DATABASE_URL=postgresql://agent_user:<password>@host.docker.internal:5433/agent_db
REDIS_URL=redis://host.docker.internal:6379/0

# 사용할 LLM provider
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
GEMINI_API_KEY=
GEMINI_MODEL=gemini-3.5-flash

# 현재 Ollama는 사용하지 않음
OLLAMA_ENABLED=false
```

실제 `.env` 파일과 API 키, DB 비밀번호는 Git에 커밋하지 않는다.

### Backend 실행

Registry 이미지를 사용하는 AWS 배포:

```bash
cd backend
docker compose -f compose.release.yml config --quiet
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker compose -f compose.release.yml ps
```

소스에서 직접 빌드하는 개발 실행:

```bash
cd backend
docker compose -f compose.yml up --build -d
```

상태 확인:

```bash
curl http://127.0.0.1:8000/health/live
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/health/ready
```

`/health/ready`는 backend뿐 아니라 PostgreSQL 연결, Redis 연결, DB 스키마까지 확인한다.

## 3. Frontend 환경변수

Frontend EC2에서 환경 파일을 만든다.

```bash
cd frontend
cp .env.example .env
```

`frontend/.env`를 다음과 같이 설정한다.

```ini
FRONTEND_IMAGE=ghcr.io/<owner>/simple-multi-llm-frontend:<tag>

# 8501을 직접 공개하려면 8501, Host 80으로 서비스하려면 80
FRONTEND_PORT=8501

# Frontend EC2에서 접근 가능한 Backend EC2 주소
BACKEND_URL=http://<backend-private-ip>:8000
```

두 EC2가 같은 VPC에 있다면 Backend EC2의 사설 IP 또는 Private DNS를 사용하는 것이
좋다. ALB나 HTTPS 도메인을 구성했다면 다음처럼 지정한다.

```ini
BACKEND_URL=https://api.example.com
```

### Frontend 실행

Registry 이미지를 사용하는 AWS 배포:

```bash
cd frontend
docker compose -f compose.release.yml config --quiet
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker compose -f compose.release.yml ps
```

소스에서 직접 빌드하는 개발 실행:

```bash
cd frontend
docker compose -f compose.yml up --build -d
```

접속 주소:

```text
FRONTEND_PORT=8501 -> http://<frontend-public-ip>:8501
FRONTEND_PORT=80   -> http://<frontend-public-ip>
```

## 4. AWS Security Group

권장 인바운드 규칙은 다음과 같다.

### Frontend EC2

| 포트 | 소스 | 용도 |
| --- | --- | --- |
| `22` | 관리자 IP | SSH |
| `80` 또는 `8501` | 사용자 또는 ALB | Streamlit |
| `443` | 사용자 또는 ALB | HTTPS 구성 시 |

### Backend EC2

| 포트 | 소스 | 용도 |
| --- | --- | --- |
| `22` | 관리자 IP | SSH |
| `8000` | Frontend EC2 프라이빗 IPv4 주소 `/32` | FastAPI |

예를 들어 Frontend EC2의 프라이빗 IPv4 주소가 `172.31.29.113`이라면 Backend EC2의
Security Group 인바운드 소스에는 `172.31.29.113/32`를 입력한다.

PostgreSQL `5433`과 Redis `6379`는 Backend EC2의 Security Group 인바운드에 추가하지
않는다. Backend EC2 내부에서만 접근하게 한다.

## 5. GitHub Actions 배포 흐름

frontend와 backend는 서로 독립적으로 빌드하고 배포한다.

```text
backend/** 변경
  -> backend 테스트
  -> backend Docker 이미지 빌드 및 push
  -> Backend EC2에서 backend/compose.release.yml 갱신

frontend/** 변경
  -> frontend 테스트
  -> frontend Docker 이미지 빌드 및 push
  -> Frontend EC2에서 frontend/compose.release.yml 갱신
```

배포 단계에서는 해당 EC2에서 다음 순서로 실행한다.

```bash
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker image prune -f
```

PostgreSQL과 Redis는 애플리케이션 CI/CD 대상이 아니다. backend 이미지를 새로 배포해도
DB와 Redis 컨테이너 및 데이터는 그대로 유지한다.

## 6. 로그와 문제 해결

Backend 로그:

```bash
cd backend
docker compose -f compose.release.yml logs -f backend
```

Frontend 로그:

```bash
cd frontend
docker compose -f compose.release.yml logs -f frontend
```

Backend가 DB 또는 Redis에 연결하지 못한다면 다음을 확인한다.

```bash
docker compose -f compose.release.yml exec backend printenv DATABASE_URL
docker compose -f compose.release.yml exec backend printenv REDIS_URL
docker compose -f compose.release.yml exec backend getent hosts host.docker.internal
```

Frontend가 backend에 연결하지 못한다면 다음을 확인한다.

```bash
docker compose -f compose.release.yml exec frontend printenv BACKEND_URL
```

그리고 Frontend EC2에서 Backend EC2로 직접 요청한다.

```bash
curl http://<backend-private-ip>:8000/health/ready
```

## 7. 종료와 재배포

Backend 애플리케이션만 종료:

```bash
cd backend
docker compose -f compose.release.yml down
```

이 명령은 별도로 실행 중인 PostgreSQL과 Redis를 중단하거나 데이터를 삭제하지 않는다.

Frontend 종료:

```bash
cd frontend
docker compose -f compose.release.yml down
```

재배포:

```bash
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
```

## 배포 확인 목록

- [ ] Frontend EC2와 Backend EC2가 같은 VPC에서 통신할 수 있다.
- [ ] Backend EC2에서 PostgreSQL과 Redis가 실행 중이다.
- [ ] `backend/.env`에서 `OLLAMA_ENABLED=false`로 설정했다.
- [ ] 실제 `.env`와 비밀값을 Git에 커밋하지 않았다.
- [ ] frontend의 `BACKEND_URL`이 Backend EC2에서 접근 가능한 주소다.
- [ ] Backend `8000` 포트는 Frontend EC2 프라이빗 IPv4 주소 `/32`에서만 접근 가능하다.
- [ ] PostgreSQL과 Redis 포트를 인터넷에 공개하지 않았다.
- [ ] backend `/health/ready`가 `status: ok`를 반환한다.
