# Lab 01. First OpenAI Call

## 목표

`gpt-4.1-mini` 모델을 사용해 OpenAI API 첫 응답을 받아봅니다.

## 준비

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
Copy-Item .env.example .env
```

`.env` 파일을 열고 다음 값을 확인합니다.

```text
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실제 OpenAI API 호출을 하려면 `OPENAI_API_KEY`에 실제 키를 넣어야 합니다. 키가 없다면 `01_check-env.py`까지만 실행합니다.

## 진행

1. `01_check-env.py`를 실행해서 `.env`가 읽히는지 확인합니다.
2. API Key가 있다면 `02_openai-basic-response.py`를 실행합니다.
3. `03_openai-message-style.py`를 실행해서 `system`, `user` 역할을 나눈 호출을 확인합니다.

```powershell
python .\01_openai-api-basic\01_check-env.py
python .\01_openai-api-basic\02_openai-basic-response.py
python .\01_openai-api-basic\03_openai-message-style.py
```

## 관찰할 내용

- API Key가 없을 때 프로그램이 오류 없이 종료되는가?
- API Key가 있을 때 실제 응답이 출력되는가?
- `system` 메시지를 넣은 예제는 기본 호출과 어떤 점이 다른가?

## 제출

- 실행한 명령
- 출력된 응답 요약
- 오류가 있었다면 해결 과정
- API Key를 코드가 아니라 `.env`에 넣는 이유
