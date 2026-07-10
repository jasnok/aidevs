# 01_prompt-design-patterns

이 챕터에서는 좋은 프롬프트를 만들기 위한 기본 패턴을 배웁니다.

## 핵심 개념

- Role은 LLM이 맡을 역할입니다.
- Instruction은 LLM이 수행할 작업입니다.
- Context는 답변에 필요한 배경 정보입니다.
- Output Format은 답변의 모양과 항목을 정합니다.
- Few-shot은 원하는 답변 예시를 먼저 보여주는 방식입니다.

## 실행 전 확인

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
Test-Path .env
```

`.env` 파일의 내용을 터미널에 그대로 출력하지 않습니다. OpenAI API Key가 없다면 예제는 실제 호출을 건너뜁니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\01_prompt-design-patterns\01_role-and-context-prompt.py
python .\01_prompt-design-patterns\02_few-shot-style-prompt.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_role-and-context-prompt.py` | 역할, 맥락, 작업, 출력 형식을 분리한 프롬프트를 실행합니다. |
| `02_few-shot-style-prompt.py` | 예시를 제공했을 때 답변 형식이 어떻게 안정되는지 확인합니다. |

## 확인 질문

- 역할을 명확히 주면 응답이 어떻게 달라지나요?
- 예시를 제공하면 왜 답변 형식이 안정될까요?
- 출력 형식을 지정하지 않으면 어떤 문제가 생길 수 있나요?
