# AWS EC2 배포 설정

이 문서는 Ubuntu 22.04/24.04 EC2 두 대에 frontend와 backend를 독립 배포하는 절차를
정리한다.

```text
Frontend EC2
  `-- Streamlit frontend container

Backend EC2
  |-- FastAPI backend container
  |-- PostgreSQL container
  `-- Redis container
```

Ollama는 사용하지 않으며 backend의 `OLLAMA_ENABLED`를 `false`로 설정한다.

명령의 `<...>` 부분은 실제 값으로 변경한다. 실제 비밀번호, API 키, registry token은
Git에 커밋하지 않는다.

## 0. 사전 준비

- Ubuntu 22.04 또는 24.04 EC2 두 대
- EC2 접속용 PEM 키
- Backend EC2 사설 IP 또는 Private DNS
- Docker Hub 또는 GitHub Container Registry에 push된 frontend/backend 이미지
- Backend EC2 루트 EBS 권장 용량: 20GB 이상

권장 Security Group 인바운드 규칙:

| 서버 | 포트 | 소스 |
| --- | --- | --- |
| Frontend EC2 | `22` | 관리자 IP |
| Frontend EC2 | `80` 또는 `8501` | 사용자 또는 ALB |
| Backend EC2 | `22` | 관리자 IP |
| Backend EC2 | `8000` | Frontend EC2 Security Group 또는 ALB |

PostgreSQL `5433`과 Redis `6379`는 Security Group에서 인터넷에 공개하지 않는다.

## 1. 서버 접속

로컬 PC에서 PEM 키 권한을 설정한다.

```bash
chmod 400 <key-name>.pem
```

Backend EC2 접속:

```bash
ssh -i <key-name>.pem ubuntu@<backend-public-ip>
```

Frontend EC2 접속:

```bash
ssh -i <key-name>.pem ubuntu@<frontend-public-ip>
```

Amazon Linux AMI를 사용했다면 사용자 이름을 `ubuntu` 대신 `ec2-user`로 변경한다.

## 2. Docker 설치

아래 작업을 Frontend EC2와 Backend EC2 양쪽에서 실행한다. 설치 방법은
[`03_install-and-transfer.md`](../03_aws-ec2/03_install-and-transfer.md)의 절차를 따른다.

### Amazon Linux 2023

```bash
sudo yum update -y
sudo yum install -y docker git
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
```

### Ubuntu Server 24.04 LTS

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2 git curl
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu
```

그룹 권한을 반영하기 위해 SSH 연결을 종료하고 다시 접속한다.

```bash
exit
```

로컬 PC에서 해당 운영체제의 사용자 이름으로 다시 접속한다.

```bash
# Ubuntu
ssh -i <key-name>.pem ubuntu@<server-public-ip>

# Amazon Linux
ssh -i <key-name>.pem ec2-user@<server-public-ip>
```

재접속 후 설치를 확인한다.

```bash
docker info
docker compose version
docker run --rm hello-world
df -h
```

Amazon Linux에서 `docker compose` 명령이 없다면 Compose Plugin을 추가로 설치한다.

```bash
sudo yum update -y
sudo yum install -y docker-compose-plugin
docker compose version
```

Ubuntu에서 `docker compose` 명령이 없다면 다음을 실행한다.

```bash
sudo apt update
sudo apt install -y docker-compose-v2
docker compose version
```

## 3. Backend EC2에 PostgreSQL과 Redis 설치

이 절부터는 Backend EC2에서만 실행한다.

### 3.1 배포 디렉터리 생성

```bash
mkdir -p ~/simple-multi-llm/backend/database
cd ~/simple-multi-llm/backend
```

### 3.2 PostgreSQL 설정 파일 생성

PostgreSQL 계정 정보를 저장할 파일을 만든다.

```bash
nano infra.env
```

다음 내용을 입력하고 `<strong-password>`를 실제 비밀번호로 변경한다.

```ini
POSTGRES_USER=agent_user
POSTGRES_PASSWORD=<strong-password>
POSTGRES_DB=agent_db
```

파일 권한을 제한한다.

```bash
chmod 600 infra.env
```

### 3.3 PostgreSQL 실행

```bash
docker volume create simple_postgres_data
docker run -d \
  --name simple-postgres \
  --restart unless-stopped \
  --env-file infra.env \
  -p 5433:5432 \
  -v simple_postgres_data:/var/lib/postgresql/data \
  postgres:17-alpine
```

준비 상태를 확인한다.

```bash
docker logs simple-postgres
docker exec simple-postgres pg_isready -U agent_user -d agent_db
```

### 3.4 Redis 실행

```bash
docker volume create simple_redis_data
docker run -d \
  --name simple-redis \
  --restart unless-stopped \
  -p 6379:6379 \
  -v simple_redis_data:/data \
  redis:7-alpine redis-server --appendonly yes
```

상태를 확인한다.

```bash
docker exec simple-redis redis-cli ping
```

정상 응답은 `PONG`이다.

## 4. 배포 파일 복사

다음 명령은 로컬 PC의 프로젝트 루트에서 실행한다.

### 4.1 Backend 파일 복사

원격 디렉터리를 먼저 만든다.

```bash
ssh -i <key-name>.pem ubuntu@<backend-public-ip> \
  "mkdir -p ~/simple-multi-llm/backend/database"
```

필요한 파일을 복사한다.

```bash
scp -i <key-name>.pem \
  backend/compose.release.yml \
  ubuntu@<backend-public-ip>:~/simple-multi-llm/backend/

scp -i <key-name>.pem \
  backend/.env.example \
  ubuntu@<backend-public-ip>:~/simple-multi-llm/backend/.env

scp -i <key-name>.pem \
  backend/database/init.sql \
  ubuntu@<backend-public-ip>:~/simple-multi-llm/backend/database/
```

### 4.2 Frontend 파일 복사

```bash
ssh -i <key-name>.pem ubuntu@<frontend-public-ip> \
  "mkdir -p ~/simple-multi-llm/frontend"
```

```bash
scp -i <key-name>.pem \
  frontend/compose.release.yml \
  ubuntu@<frontend-public-ip>:~/simple-multi-llm/frontend/

scp -i <key-name>.pem \
  frontend/.env.example \
  ubuntu@<frontend-public-ip>:~/simple-multi-llm/frontend/.env
```

Windows PowerShell에서도 `ssh`와 `scp` 명령 형식은 동일하며 PEM 파일은 전체 경로로
지정할 수 있다.

## 5. 환경변수 설정

### 5.1 Backend `.env`

Backend EC2에서 실행한다.

```bash
cd ~/simple-multi-llm/backend
nano .env
```

다음 값을 실제 환경에 맞게 설정한다. PostgreSQL 비밀번호는 `infra.env`와 같아야 한다.

```ini
BACKEND_IMAGE=ghcr.io/<owner>/simple-multi-llm-backend:<tag>
BACKEND_PORT=8000

DATABASE_URL=postgresql://agent_user:<strong-password>@host.docker.internal:5433/agent_db
REDIS_URL=redis://host.docker.internal:6379/0

OPENAI_API_KEY=<openai-api-key>
OPENAI_MODEL=gpt-4.1-mini
GEMINI_API_KEY=<gemini-api-key>
GEMINI_MODEL=gemini-3.5-flash

OLLAMA_ENABLED=false
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=llama3.2:1b
GEMMA_MODEL=gemma3:1b
```

사용하지 않는 provider의 API 키는 빈 값으로 둔다. Ollama 관련 모델 값은
`OLLAMA_ENABLED=false`일 때 사용되지 않는다.

```bash
chmod 600 .env
```

### 5.2 Frontend `.env`

Frontend EC2에서 실행한다.

```bash
cd ~/simple-multi-llm/frontend
nano .env
```

```ini
FRONTEND_IMAGE=ghcr.io/<owner>/simple-multi-llm-frontend:<tag>
FRONTEND_PORT=8501
BACKEND_URL=http://<backend-private-ip>:8000
```

공개 도메인과 HTTPS를 구성했다면 다음처럼 설정한다.

```ini
BACKEND_URL=https://api.example.com
```

```bash
chmod 600 .env
```

## 6. 데이터베이스 스키마 설치

Backend EC2에서 PostgreSQL 컨테이너에 스키마를 적용한다.

```bash
cd ~/simple-multi-llm/backend
docker exec -i simple-postgres \
  psql -U agent_user -d agent_db < database/init.sql
```

테이블을 확인한다.

```bash
docker exec simple-postgres \
  psql -U agent_user -d agent_db \
  -c "\dt simple_multi_llm.*"
```

`notes`, `chat_messages` 테이블이 표시되어야 한다. `init.sql`은 `IF NOT EXISTS`를
사용하므로 다시 실행해도 기존 테이블을 삭제하지 않는다.

## 7. Container Registry 로그인

배포 이미지가 공개 이미지라면 로그인이 필요하지 않다. 비공개 이미지라면 각 EC2에서
registry에 로그인한다.

### Docker Hub

```bash
docker login
```

사용자명과 access token을 입력한다. 계정 비밀번호보다 access token 사용을 권장한다.

### GitHub Container Registry

GitHub Personal Access Token은 최소 `read:packages` 권한이 필요하다.

```bash
read -s GHCR_TOKEN
echo "$GHCR_TOKEN" | docker login ghcr.io -u <github-username> --password-stdin
unset GHCR_TOKEN
```

로그인 성공 여부를 확인한다.

```bash
docker info | grep Username
```

## 8. Backend Docker Compose 실행

Backend EC2에서 실행한다.

```bash
cd ~/simple-multi-llm/backend
docker compose -f compose.release.yml config --quiet
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker compose -f compose.release.yml ps
```

로그와 health endpoint를 확인한다.

```bash
docker compose -f compose.release.yml logs -f backend
```

별도 SSH 창에서:

```bash
curl http://127.0.0.1:8000/health/live
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/health/ready
```

`/health/ready`가 `status: ok`를 반환해야 frontend 배포를 진행한다.

## 9. Frontend Docker Compose 실행

Frontend EC2에서 실행한다.

```bash
cd ~/simple-multi-llm/frontend
docker compose -f compose.release.yml config --quiet
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker compose -f compose.release.yml ps
```

Frontend EC2에서 backend 연결을 먼저 확인한다.

```bash
curl http://<backend-private-ip>:8000/health/ready
```

Frontend 로그를 확인한다.

```bash
docker compose -f compose.release.yml logs -f frontend
```

접속 주소:

```text
FRONTEND_PORT=8501 -> http://<frontend-public-ip>:8501
FRONTEND_PORT=80   -> http://<frontend-public-ip>
```

## 10. 재배포

GitHub Actions가 새 이미지를 push한 뒤 해당 EC2에서 실행할 명령이다.

```bash
docker compose -f compose.release.yml pull
docker compose -f compose.release.yml up -d
docker image prune -f
```

backend와 frontend의 작업 디렉터리는 서로 다르지만 재배포 명령은 같다.

## 11. 종료 및 상태 확인

애플리케이션 컨테이너 종료:

```bash
docker compose -f compose.release.yml down
```

Backend EC2에서 위 명령은 backend 애플리케이션만 종료한다. 별도로 실행한 PostgreSQL과
Redis는 계속 실행된다.

전체 Docker 상태 확인:

```bash
docker ps
docker system df
df -h
```

PostgreSQL 또는 Redis를 직접 재시작해야 할 때만 다음을 실행한다.

```bash
docker restart simple-postgres
docker restart simple-redis
```

데이터가 저장된 `simple_postgres_data`, `simple_redis_data` 볼륨은 삭제하지 않는다.
특히 운영 서버에서 `docker system prune --volumes`를 실행하면 안 된다.

## 최종 확인

```text
[ ] Frontend EC2와 Backend EC2에 Docker/Compose가 설치되었다.
[ ] Backend EC2에서 PostgreSQL과 Redis가 healthy 상태다.
[ ] database/init.sql이 적용되었다.
[ ] backend/.env의 OLLAMA_ENABLED=false를 확인했다.
[ ] 각 EC2에서 container registry 로그인이 완료되었다.
[ ] backend /health/ready가 status: ok를 반환한다.
[ ] Frontend EC2에서 Backend EC2의 :8000에 접근할 수 있다.
[ ] PostgreSQL과 Redis 포트는 인터넷에 공개되지 않았다.
[ ] 실제 .env, infra.env, API 키, DB 비밀번호는 Git에 커밋하지 않았다.
```
