# 05 Local Environment Checklist

이 과정은 Python, Docker, OpenAI API, Ollama, PostgreSQL/pgvector, Redis, LangGraph를 사용합니다.

수업 전에 아래 항목을 확인하면 실습 중 오류를 줄일 수 있습니다.

## Python

```powershell
python --version
pip --version
```

권장:

```text
Python 3.11 이상
```

## 가상 환경

05 과정은 단원별 가상 환경을 우선 권장합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
```

`python -c "import sys; print(sys.executable)"` 결과가 현재 단원 폴더의 `.venv\Scripts\python.exe`를 가리키는지 확인합니다.

## Docker

Docker Desktop이 설치되어 있어야 합니다.

```powershell
docker --version
docker ps
```

Docker Desktop이 실행 중이어야 합니다.

Docker를 처음 설치했다면 아래 문서를 먼저 확인합니다.

```text
00_references/09_docker-desktop-install-for-beginners.md
```

설치 후에는 기본 테스트 컨테이너를 한 번 실행해 봅니다.

```powershell
docker run hello-world
```

`hello-world` 컨테이너는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

## OpenAI API Key

OpenAI 호출 실습을 하려면 `.env` 파일에 다음 값이 있어야 합니다.

```text
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

API Key가 없어도 Ollama, mock Tool, 일부 LangGraph 예제는 진행할 수 있습니다.

## Ollama

로컬 Llama 비교 실습에서는 Ollama 컨테이너를 선택적으로 사용합니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

## pgvector

RAG와 장기 기억 실습에서는 PostgreSQL + pgvector 컨테이너를 사용합니다.

PostgreSQL은 PC에 직접 설치하지 않고, pgvector가 포함된 PostgreSQL Docker 컨테이너로 실행합니다.

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

접속 확인:

```powershell
docker exec -it aidev-pgvector psql -U agent_user -d agent_db
```

## Redis

세션 메모리와 캐시 실습에서는 Redis 컨테이너를 사용합니다.

```powershell
docker run -d `
  --name aidev-redis `
  -p 6379:6379 `
  redis:7
```

동작 확인:

```powershell
docker exec -it aidev-redis redis-cli ping
```

정상이라면 `PONG`이 출력됩니다.

## 자주 사용하는 포트

| 포트 | 용도 |
| --- | --- |
| 11434 | Ollama |
| 5433 | PostgreSQL + pgvector |
| 6379 | Redis |
| 8601 | 99 샘플 Streamlit 앱 |

## 수업 전 최종 체크

- [ ] Python이 설치되어 있다.
- [ ] Docker Desktop이 설치되어 있다.
- [ ] Docker Desktop이 실행된다.
- [ ] `docker --version`이 정상 동작한다.
- [ ] `docker ps`가 오류 없이 실행된다.
- [ ] `docker run hello-world`가 성공한다.
- [ ] OpenAI API Key 또는 Ollama 선택 실습 기준을 이해했다.
- [ ] `.env` 파일을 만들 수 있다.
- [ ] PowerShell에서 가상 환경을 활성화할 수 있다.
- [ ] 브라우저에서 localhost 주소를 열 수 있다.
