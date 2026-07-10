# Lab 02. Local Llama With Docker

## 목표

Docker Desktop에서 Ollama 컨테이너를 실행하고 로컬 Llama 응답을 확인합니다.

## 준비

Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

`docker ps`가 오류 없이 실행되면 Docker Desktop이 정상 동작 중입니다.

## 진행

1. Ollama 컨테이너를 실행합니다.

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

이미 `ollama-llm` 컨테이너가 있다고 나오면 아래 명령으로 다시 시작합니다.

```powershell
docker start ollama-llm
```

2. Llama 모델을 다운로드합니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
docker exec -it ollama-llm ollama list
```

3. Python 예제를 실행합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
python .\02_ollama-docker-llama\01_ollama-health-check.py
python .\02_ollama-docker-llama\02_ollama-generate.py
```

## 관찰할 내용

- `01_ollama-health-check.py`에서 모델 목록 JSON이 출력되는가?
- `02_ollama-generate.py`에서 Llama 응답이 출력되는가?
- OpenAI API Key 없이도 로컬 Llama 호출이 가능한가?

## 제출

- `docker ps` 확인 결과
- Llama 응답 예시
- OpenAI API와 비교했을 때 느낀 차이
- 오류가 있었다면 어떤 명령에서 발생했는지와 해결 방법
