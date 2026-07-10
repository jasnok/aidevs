# 01 Docker Run Troubleshooting

05 과정에서는 Docker Compose가 아니라 `docker run`으로 필요한 컨테이너를 하나씩 실행합니다.

## 기본 확인

```powershell
docker --version
docker ps
docker ps -a
```

## 컨테이너 이름 충돌

이미 같은 이름의 컨테이너가 있으면 새로 만들 수 없습니다.

```powershell
docker ps -a
docker start aidev-pgvector
docker start aidev-redis
```

삭제 후 다시 만들려면:

```powershell
docker stop aidev-pgvector aidev-redis
docker rm aidev-pgvector aidev-redis
```

## 포트 충돌

```powershell
netstat -ano | findstr :5433
netstat -ano | findstr :6379
netstat -ano | findstr :11434
```

포트를 바꾸면 `.env`의 `DATABASE_URL`, `REDIS_URL`, `OLLAMA_BASE_URL`도 함께 바꿔야 합니다.
