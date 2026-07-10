# 01_function-calling-basic

이 챕터에서는 LLM이 사용할 수 있는 Python 함수를 Tool로 설계하는 기본 흐름을 학습합니다.

## 핵심 개념

- Function Calling은 LLM이 필요한 기능을 선택해 호출하도록 만드는 구조입니다.
- 실제 계산이나 데이터 처리는 Python 함수가 담당합니다.
- LLM은 어떤 Tool이 필요한지 판단하고, Tool 결과를 바탕으로 응답합니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\01_function-calling-basic\01_simple-calculator-tool.py
python .\01_function-calling-basic\02_learning-log-summary-tool.py
```

## 확인 질문

- 계산은 왜 LLM이 직접 하지 않고 Tool에 맡기는 것이 좋을까요?
- Tool 입력과 출력은 왜 명확해야 할까요?

