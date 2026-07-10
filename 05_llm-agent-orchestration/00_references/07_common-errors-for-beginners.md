# 07 Common Errors for Beginners

이 문서는 초보자가 자주 만나는 오류를 정리합니다.

## 1. OPENAI_API_KEY가 없다는 오류

원인:

- `.env` 파일이 없다.
- `.env` 파일 위치가 잘못되었다.
- `OPENAI_API_KEY` 이름을 다르게 썼다.
- 가상 환경에서 필요한 패키지를 설치하지 않았다.

확인:

```text
.env 파일이 현재 단원 폴더에 있는가?
OPENAI_API_KEY=... 형태로 작성했는가?
```

API Key가 없으면 OpenAI 호출 예제는 건너뛰고, Ollama 또는 mock 예제부터 진행할 수 있습니다.

## 2. ModuleNotFoundError

예시:

```text
ModuleNotFoundError: No module named 'langgraph'
```

해결:

```powershell
.\.venv\Scripts\Activate.ps1
pip install langgraph
```

또는 README의 설치 명령을 다시 실행합니다.

## 3. Docker 컨테이너 이름 충돌

예시:

```text
Conflict. The container name is already in use.
```

해결:

```powershell
docker ps -a
docker stop 컨테이너이름
docker rm 컨테이너이름
```

컨테이너를 삭제하고 싶지 않다면 다시 시작합니다.

```powershell
docker start 컨테이너이름
```

## 4. docker 명령을 찾을 수 없는 경우

예시:

```text
docker : The term 'docker' is not recognized
```

원인:

- Docker Desktop이 설치되지 않았다.
- Docker Desktop 설치 후 PowerShell을 다시 열지 않았다.
- 설치 후 PC 재부팅이 필요하다.

해결:

```text
1. Docker Desktop 설치 여부를 확인한다.
2. Docker Desktop을 실행한다.
3. PowerShell을 닫고 다시 연다.
4. docker --version을 다시 실행한다.
5. 계속 실패하면 PC를 재부팅한다.
```

## 5. Docker daemon 오류가 나는 경우

예시:

```text
Cannot connect to the Docker daemon
```

원인:

- Docker Desktop이 실행되지 않았다.
- Docker Engine이 아직 시작 중이다.
- WSL 2 백엔드가 정상 준비되지 않았다.

해결:

```text
1. Docker Desktop을 실행한다.
2. Docker Desktop 상태가 정상 실행 상태가 될 때까지 기다린다.
3. docker ps를 다시 실행한다.
4. 계속 실패하면 Docker Desktop을 재시작한다.
5. 그래도 실패하면 PC를 재부팅한다.
```

WSL 상태 확인:

```powershell
wsl --status
wsl --list --verbose
```

## 6. 포트 충돌

예시:

```text
port is already allocated
```

확인:

```powershell
netstat -ano | findstr :11434
netstat -ano | findstr :5433
netstat -ano | findstr :6379
```

기본 포트:

| 포트 | 용도 |
| --- | --- |
| `11434` | Ollama |
| `5433` | PostgreSQL + pgvector |
| `6379` | Redis |

해결:

- 기존 프로그램을 종료한다.
- 기존 컨테이너가 있다면 `docker start`로 재사용한다.
- 다른 포트를 사용한다면 `.env`의 URL도 함께 바꾼다.

## 7. Ollama 모델이 없다는 오류

원인:

- 컨테이너는 실행했지만 모델을 다운로드하지 않았다.

해결:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

## 8. pgvector extension이 없다는 오류

원인:

- 일반 PostgreSQL 이미지를 사용했다.
- `CREATE EXTENSION vector;`를 실행하지 않았다.

권장 컨테이너:

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

SQL:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

일반 `postgres` 이미지를 사용하면 pgvector 확장이 없어서 오류가 날 수 있습니다. 05 과정에서는 `pgvector/pgvector:pg16` 이미지를 사용합니다.

## 9. Redis 연결 오류

예시:

```text
Error connecting to localhost:6379
```

확인:

```powershell
docker ps
docker exec -it aidev-redis redis-cli ping
```

정상이라면 `PONG`이 출력됩니다.

실행:

```powershell
docker run -d `
  --name aidev-redis `
  -p 6379:6379 `
  redis:7
```

## 10. Streamlit 버튼을 누를 때마다 비용이 발생할 수 있음

Streamlit은 버튼을 누르거나 입력값이 바뀔 때 스크립트를 다시 실행할 수 있습니다.

LLM API 호출 코드는 버튼 클릭 안쪽에 두는 것이 좋습니다.

## 11. 그래프가 예상과 다르게 흐르는 경우

확인할 것:

- State 필드명이 맞는가?
- Node가 dict를 반환하는가?
- Conditional Edge 함수가 올바른 노드 이름을 반환하는가?
- START와 END 연결이 빠지지 않았는가?
- Retry 조건이 무한 반복을 만들지 않는가?
