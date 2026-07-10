# 03 pgvector and Redis Errors

## pgvector 확인

컨테이너 상태:

```powershell
docker ps
docker exec -it aidev-pgvector psql -U agent_user -d agent_db
```

Python 코드의 기본 접속 문자열:

```text
DATABASE_URL=postgresql://agent_user:agent_password@localhost:5433/agent_db
```

pgvector 확장 확인:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

## Redis 확인

```powershell
docker ps
docker exec -it aidev-redis redis-cli ping
```

정상 출력:

```text
PONG
```

Python 코드의 기본 접속 문자열:

```text
REDIS_URL=redis://localhost:6379/0
```

## 자주 생기는 원인

- 컨테이너가 실행되지 않았다.
- 포트가 다르다.
- `.env`의 URL이 SETUP 명령과 다르다.
- 가상환경에 `psycopg[binary]` 또는 `redis`가 설치되지 않았다.
