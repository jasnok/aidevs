# 06 Docker, Ollama, pgvector, Redis Overview

05 과정에서 Docker는 로컬 실습 도구를 실행하기 위해 사용합니다.

```text
Ollama                -> 로컬 Llama 실행
PostgreSQL + pgvector -> RAG, 벡터 검색, 장기 기억
Redis                 -> 세션 메모리, 캐시
```

## Docker Compose를 꼭 써야 하나요?

아니요. 05 과정에서는 Docker Compose를 사용하지 않습니다.

서비스 하나를 실행할 때는 `docker run`이 초보자에게 더 직접적입니다.

```text
Ollama 하나 실행              -> docker run
PostgreSQL + pgvector 하나 실행 -> docker run
Redis 하나 실행               -> docker run
여러 서비스를 묶어 운영         -> 07 과정에서 Docker Compose
```

## Ollama

Ollama는 로컬에서 Llama 같은 모델을 실행할 수 있게 해줍니다.

실행:

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

확인:

```powershell
docker exec -it ollama-llm ollama list
```

모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

## PostgreSQL + pgvector

pgvector는 PostgreSQL에서 벡터를 저장하고 검색할 수 있게 해주는 확장입니다. 05 과정에서는 PostgreSQL을 직접 설치하지 않고, pgvector가 포함된 Docker 이미지를 사용합니다.

실행:

```powershell
docker run -d `
  --name aidev-pgvector `
  -p 5433:5432 `
  -e POSTGRES_DB=agent_db `
  -e POSTGRES_USER=agent_user `
  -e POSTGRES_PASSWORD=agent_password `
  -v aidev-pgvector-data:/var/lib/postgresql/data `
  pgvector/pgvector:pg16
```

확인:

```powershell
docker exec -it aidev-pgvector psql -U agent_user -d agent_db
```

## Redis

Redis는 빠르게 읽고 쓰는 임시 저장소입니다. 05 과정에서는 세션 메모리와 캐시를 설명할 때 사용합니다.

실행:

```powershell
docker run -d `
  --name aidev-redis `
  -p 6379:6379 `
  redis:7
```

확인:

```powershell
docker exec -it aidev-redis redis-cli ping
```

## 컨테이너 중지와 재시작

중지:

```powershell
docker stop ollama-llm aidev-pgvector aidev-redis
```

재시작:

```powershell
docker start ollama-llm aidev-pgvector aidev-redis
```

삭제:

```powershell
docker rm ollama-llm aidev-pgvector aidev-redis
```

데이터 volume까지 삭제:

```powershell
docker volume rm ollama-data aidev-pgvector-data
```

## 초보자 주의점

- Docker Desktop이 켜져 있어야 합니다.
- 같은 이름의 컨테이너가 이미 있으면 새로 만들 수 없습니다.
- 같은 포트를 다른 프로그램이 쓰고 있으면 실행이 실패합니다.
- 모델과 DB 데이터는 Docker volume에 저장합니다.
- volume을 삭제하면 모델 파일과 PostgreSQL 데이터가 함께 사라집니다.
- Docker Compose는 05에서 쓰지 않고 07에서 배웁니다.
