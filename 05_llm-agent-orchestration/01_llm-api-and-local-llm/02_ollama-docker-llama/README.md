# 02_ollama-docker-llama

이 챕터에서는 Docker Desktop에서 Ollama 컨테이너를 실행하고 로컬 Llama 모델을 호출합니다.

## 핵심 개념

- Ollama는 로컬 LLM을 쉽게 실행하게 해주는 도구입니다.
- 05 과정에서는 Ollama를 PC에 직접 설치하지 않고 Docker 컨테이너로 실행합니다.
- OpenAI API와 달리 로컬 Llama는 내 PC의 자원을 사용합니다.
- Python 코드는 `http://localhost:11434` 주소로 Ollama REST API를 호출합니다.

## 실행 전 준비

Docker Desktop을 먼저 실행합니다.

```powershell
docker --version
docker ps
```

Ollama 컨테이너가 없다면 다음 명령으로 실행합니다.

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

Llama 모델을 다운로드합니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

컨테이너와 모델 상태를 확인합니다.

```powershell
docker ps
docker exec -it ollama-llm ollama list
```

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
python .\02_ollama-docker-llama\01_ollama-health-check.py
python .\02_ollama-docker-llama\02_ollama-generate.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_ollama-health-check.py` | Ollama 서버가 켜져 있는지 `/api/tags`로 확인합니다. |
| `02_ollama-generate.py` | `/api/generate`로 Llama 모델에 프롬프트를 보내고 응답을 받습니다. |

## 자주 나는 오류

| 상황 | 확인할 내용 |
| --- | --- |
| 연결 실패 | Docker Desktop이 실행 중인지, `ollama-llm` 컨테이너가 켜져 있는지 확인합니다. |
| 모델 없음 | `docker exec -it ollama-llm ollama pull llama3.2`를 먼저 실행합니다. |
| 포트 충돌 | 다른 프로그램이 `11434` 포트를 사용 중인지 확인합니다. |

## 확인 질문

- Docker 컨테이너는 어떤 역할을 하나요?
- 로컬 Llama는 인터넷 API 호출과 무엇이 다른가요?
- Ollama 서버가 켜져 있는지 어떻게 확인할 수 있나요?
- `localhost:11434`는 어떤 의미인가요?
