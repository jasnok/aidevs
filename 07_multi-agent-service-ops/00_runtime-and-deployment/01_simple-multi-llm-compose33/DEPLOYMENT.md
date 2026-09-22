# Compose33 AWS Ubuntu 배포 준비

Frontend, Backend, PostgreSQL/pgvector, Redis를 한 Ubuntu 서버에서 실행한다.
PostgreSQL과 Redis는 외부 포트를 공개하지 않고 `compose33-shared` Docker 네트워크에서만
Backend와 통신한다. Backend와 Frontend는 서로 독립된 GitHub Actions로 배포한다.

## 1. Ubuntu 준비

Docker가 없다면 다음 명령으로 설치한다.

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2 git curl
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu
exit
```

다시 SSH로 접속한 뒤 확인한다.

```bash
docker --version
docker compose version
docker run --rm hello-world
mkdir -p ~/compose33/backend ~/compose33/frontend
```

## 2. 서버 환경 파일 준비

GitHub Actions는 비밀 환경 파일을 생성하거나 덮어쓰지 않는다. 다음 세 파일을 서버에 최초
한 번 준비한다.

`~/compose33/infrastructure.env`:

```dotenv
POSTGRES_USER=agent_user
POSTGRES_PASSWORD=<강한 비밀번호>
POSTGRES_DB=agent_db
```

`~/compose33/backend/.env.docker`:

```dotenv
OPENAI_API_KEY=<실제 키 또는 빈 값>
OPENAI_MODEL=gpt-4.1-mini
GEMINI_API_KEY=<실제 키 또는 빈 값>
GEMINI_MODEL=gemini-3.5-flash
DATABASE_URL=postgresql://agent_user:<위와 같은 URL 인코딩 비밀번호>@database:5432/agent_db
REDIS_URL=redis://redis:6379/0
OLLAMA_ENABLED=false
BACKEND_IMAGE=jso4603/simple-backend:compose33-latest
BACKEND_PORT=8000
```

`~/compose33/frontend/.env.docker`:

```dotenv
BACKEND_URL=http://backend:8000
FRONTEND_IMAGE=jso4603/simple-frontend:compose33-latest
FRONTEND_PORT=8501
```

권한을 제한한다.

```bash
chmod 600 ~/compose33/infrastructure.env
chmod 600 ~/compose33/backend/.env.docker
chmod 600 ~/compose33/frontend/.env.docker
```

## 3. GitHub wk01 Environment

다음 Environment Secret을 등록한다.

| Secret | 값 |
| --- | --- |
| `AWS_HOST` | Ubuntu 서버 Public IPv4 또는 DNS |
| `AWS_USER` | `ubuntu` |
| `AWS_SSH_PRIVATE_KEY` | PEM 개인 키 전체 내용 |
| `AWS_SSH_KNOWN_HOSTS` | 검증된 `ssh-ed25519` known_hosts 한 줄 |
| `DOCKERHUB_USERNAME` | `jso4603` |
| `DOCKERHUB_TOKEN` | Docker Hub Access Token |

Docker Hub에 `jso4603/simple-backend`, `jso4603/simple-frontend` 저장소가 있어야 한다.

## 4. 최초 배포 순서

1. `07 Compose33 Backend CI CD`를 먼저 실행한다. 이 Workflow가 pgvector와 Redis, 공용
   Network를 만들고 Backend를 배포한다.
2. Backend의 `/health/ready`가 성공한 뒤 `07 Compose33 Frontend CI CD`를 실행한다.
3. 이후에는 Backend 또는 Frontend 변경 경로에 따라 해당 Workflow만 자동 실행된다.

서버에서 상태를 확인한다.

```bash
docker ps
docker exec compose33-pgvector pg_isready -U agent_user -d agent_db
docker exec compose33-redis redis-cli ping
curl --fail http://127.0.0.1:8000/health/ready
curl --fail http://127.0.0.1:8501/_stcore/health
```

브라우저에서는 다음 주소를 확인한다.

```text
http://<AWS_PUBLIC_IP>:8000/docs
http://<AWS_PUBLIC_IP>:8501
```

PostgreSQL과 Redis의 `5432`, `6379`는 AWS Security Group에 열지 않는다. 사용자 접속용
`8000`, `8501`은 필요한 IP만 허용한다. GitHub-hosted Runner가 SSH 배포할 때는 실행 시점에
서버의 22번 포트로 접근할 수 있어야 한다.

## 5. 데이터 유지

Backend와 Frontend 배포는 `compose33-pgvector`, `compose33-redis`와 다음 Volume을 삭제하지
않는다.

```text
compose33-postgres-data
compose33-redis-data
```

`docker compose down -v` 또는 `docker volume rm`은 저장된 DB와 Redis 데이터를 삭제하므로
초기화가 명확히 필요한 경우가 아니면 실행하지 않는다.
