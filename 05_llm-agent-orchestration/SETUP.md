# SETUP

`05_llm-agent-orchestration` 과정의 개발 환경 설정 문서입니다.

05 과정은 Docker를 사용하지만 Docker 운영 과정은 아닙니다. 여기서는 Agent 실습에 필요한 도구를 `docker run`으로 하나씩 실행합니다. Docker Compose, Dockerfile, AWS, GitHub Actions는 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 0. 공통 준비 문서

아래 항목이 아직 준비되지 않았다면 먼저 공통 설치 가이드를 확인합니다.

| 필요한 내용 | 문서 |
| --- | --- |
| Python과 `.venv` | [`../00_course-guide/02_setup-guides/01_python-install-guide.md`](../00_course-guide/02_setup-guides/01_python-install-guide.md), [`../00_course-guide/02_setup-guides/06_venv-pip-requirements-guide.md`](../00_course-guide/02_setup-guides/06_venv-pip-requirements-guide.md) |
| OpenAI 계정, API Key, 비용 | [`../00_course-guide/02_setup-guides/08_gemini-openai-account-guide.md`](../00_course-guide/02_setup-guides/08_gemini-openai-account-guide.md) |
| Docker Desktop | [`../00_course-guide/02_setup-guides/14_docker-desktop-guide.md`](../00_course-guide/02_setup-guides/14_docker-desktop-guide.md) |
| `.env`와 secret 보안 | [`../00_course-guide/02_setup-guides/07_env-and-secret-guide.md`](../00_course-guide/02_setup-guides/07_env-and-secret-guide.md) |
| Codex와 ChatGPT 사용 준비 | [`../00_course-guide/02_setup-guides/17_codex-chatgpt-guide.md`](../00_course-guide/02_setup-guides/17_codex-chatgpt-guide.md) |
| 문제 해결 | [`../00_course-guide/03_learning-support/troubleshooting.md`](../00_course-guide/03_learning-support/troubleshooting.md) |

## 1. 작업 위치

```powershell
cd C:\aidev\05_llm-agent-orchestration
```

## 2. 가상환경 기준

수업 기본 흐름은 단원별 `.venv`를 우선합니다.

```text
01~04 과정: 과정 최상위 .venv 하나 사용
05 과정   : 단원별 .venv 우선 권장
06~08 과정: 과정 최상위 .venv 하나 사용
```

예를 들어 첫 단원은 다음처럼 시작합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
```

정상이라면 `python -c "import sys; print(sys.executable)"` 결과가 현재 단원 폴더 아래의 Python을 가리켜야 합니다.

```text
C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\.venv\Scripts\python.exe
```

복습이나 통합 실습을 위해 하나의 가상환경으로 진행하려면 최상위 `requirements.txt`를 사용할 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. .env 작성

최상위 예시는 다음 파일입니다.

```powershell
Copy-Item .env.example .env
```

단원별 예제가 별도의 `.env.example`을 제공하면 해당 단원 폴더 안에서도 `.env`를 만들 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
Copy-Item .env.example .env
```

`.env` 파일에는 실제 API Key가 들어갈 수 있으므로 GitHub에 올리지 않습니다.

## 4. Docker Desktop 확인

Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

`docker ps`가 오류 없이 실행되면 컨테이너를 실행할 준비가 된 것입니다.

## 5. 선택: Ollama 컨테이너 실행

Ollama는 로컬 Llama 모델 비교 실습에 사용합니다. PC 사양이나 수업 시간에 따라 선택적으로 진행합니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

모델을 다운로드합니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
docker exec -it ollama-llm ollama list
```

이미 컨테이너가 있다면 다시 만들지 말고 시작합니다.

```powershell
docker start ollama-llm
```

## 6. pgvector 컨테이너 실행

RAG, Vector DB, Long-term Memory 실습에서는 PostgreSQL + pgvector 컨테이너를 사용합니다.

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

컨테이너 안의 `psql`에서 빠져나올 때는 다음을 입력합니다.

```text
\q
```

## 7. Redis 컨테이너 실행

Redis는 세션 메모리, 캐시, 짧은 상태 저장 실습에 사용합니다.

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

정상이라면 다음처럼 출력됩니다.

```text
PONG
```

## 8. 포트 충돌 확인

컨테이너 실행이 실패하면 이미 같은 포트를 사용하는 프로그램이 있을 수 있습니다.

```powershell
netstat -ano | findstr :11434
netstat -ano | findstr :5433
netstat -ano | findstr :6379
```

05 과정의 기본 포트는 다음과 같습니다.

| 포트 | 용도 |
| --- | --- |
| `11434` | Ollama |
| `5433` | PostgreSQL + pgvector |
| `6379` | Redis |

## 9. 컨테이너 관리

실습을 잠시 멈출 때:

```powershell
docker stop ollama-llm aidev-pgvector aidev-redis
```

다시 시작할 때:

```powershell
docker start ollama-llm aidev-pgvector aidev-redis
```

컨테이너를 삭제할 때:

```powershell
docker rm ollama-llm aidev-pgvector aidev-redis
```

데이터까지 삭제할 때는 volume을 지웁니다. 이 명령은 저장된 모델, DB 데이터, Redis 데이터가 사라질 수 있으므로 수업 중에는 신중하게 사용합니다.

```powershell
docker volume rm ollama-data aidev-pgvector-data
```

## 체크리스트

```text
[ ] 현재 작업 위치가 C:\aidev\05_llm-agent-orchestration 인가?
[ ] 단원별 .venv 기준을 확인했는가?
[ ] python -c "import sys; print(sys.executable)" 결과가 현재 단원의 .venv를 가리키는가?
[ ] .env 파일을 만들었고 Git에 올리지 않는다는 점을 이해했는가?
[ ] Docker Desktop이 실행 중인가?
[ ] docker ps가 오류 없이 실행되는가?
[ ] 필요한 단원에서 Ollama, pgvector, Redis 컨테이너를 실행할 수 있는가?
```
