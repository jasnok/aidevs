# 01_openai-api-basic

이 챕터에서는 OpenAI API를 Python에서 처음 호출하는 흐름을 배웁니다.

OpenAI API Key가 없다면 이 챕터의 코드는 실제 호출을 하지 않고 안전하게 종료됩니다. 따라서 먼저 파일을 실행해 보면서 `.env`를 읽는 흐름과 오류가 나지 않게 종료하는 방식을 확인할 수 있습니다.

## 핵심 개념

- `.env` 파일에서 `OPENAI_API_KEY`와 `OPENAI_MODEL`을 읽습니다.
- 기본 모델은 `gpt-4.1-mini`를 사용합니다.
- API Key가 없을 때 예제가 어떻게 안전하게 종료되는지 확인합니다.
- 메시지 스타일을 바꾸면 응답이 어떻게 달라지는지 살펴봅니다.

## 실행 전 확인

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
Test-Path .env
python .\01_openai-api-basic\01_check-env.py
```

`.env` 파일의 내용을 터미널에 그대로 출력하지 않습니다. 실제 키가 들어 있다면 OpenAI 호출 예제가 실행됩니다. 아직 키가 없다면 `01_check-env.py`로 상태만 확인하고, OpenAI 호출 예제는 건너뛴 뒤 `02_ollama-docker-llama`로 넘어가도 됩니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
python .\01_openai-api-basic\01_check-env.py
python .\01_openai-api-basic\02_openai-basic-response.py
python .\01_openai-api-basic\03_openai-message-style.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_check-env.py` | `.env` 파일에서 OpenAI API Key와 모델명을 읽을 수 있는지 확인합니다. |
| `02_openai-basic-response.py` | 가장 단순한 문자열 입력으로 OpenAI 응답을 받아봅니다. |
| `03_openai-message-style.py` | `system`, `user` 역할을 나누어 요청하는 방법을 확인합니다. |

## 확인 질문

- 환경 변수는 왜 코드에 직접 적지 않을까요?
- `gpt-4.1-mini`는 어떤 실습에 적합할까요?
- API 호출 실패 시 무엇을 먼저 확인해야 할까요?
- `system` 메시지와 `user` 메시지는 각각 어떤 역할을 하나요?
