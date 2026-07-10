# 02_tool-use-with-external-api

이 챕터에서는 외부 API나 외부 데이터를 Tool처럼 사용하는 방법을 배웁니다.

## 핵심 개념

- 외부 API는 날씨, 일정, 검색, 업무 데이터처럼 LLM 밖에 있는 정보를 가져옵니다.
- Tool wrapper는 외부 API 호출을 Agent가 이해하기 쉬운 함수로 감싸는 방식입니다.
- 먼저 Mock Tool로 구조를 이해하고, 이후 HTTP API Tool로 확장합니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\02_tool-use-with-external-api\01_mock-weather-tool.py
python .\02_tool-use-with-external-api\02_http-api-tool-wrapper.py
```

## 확인 질문

- Mock API로 먼저 실습하는 이유는 무엇인가요?
- 외부 API가 실패하면 Agent는 어떻게 대응해야 할까요?

