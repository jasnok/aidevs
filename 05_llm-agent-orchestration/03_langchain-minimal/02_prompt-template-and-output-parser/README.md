# 02_prompt-template-and-output-parser

이 챕터에서는 PromptTemplate, ChatPromptTemplate, Structured Output을 학습합니다.

## 핵심 개념

- PromptTemplate은 반복되는 프롬프트 형식을 관리합니다.
- ChatPromptTemplate은 역할 기반 메시지 구성을 쉽게 만듭니다.
- Structured Output은 LLM 응답을 Pydantic 모델로 검증합니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\03_langchain-minimal
.\.venv\Scripts\Activate.ps1
python .\02_prompt-template-and-output-parser\01_prompt-template-basic.py
python .\02_prompt-template-and-output-parser\02_chat-prompt-template.py
python .\02_prompt-template-and-output-parser\03_structured-output-parser.py
```

## 확인 질문

- 프롬프트 템플릿을 쓰면 어떤 반복 작업이 줄어드나요?
- Structured Output은 일반 JSON 요청보다 어떤 점이 안정적인가요?

