# Lab 01. Calculator Tool

## 목표

계산 작업을 LLM이 직접 처리하지 않고 Python Tool에 맡기는 구조를 이해합니다.

## 진행

1. 계산 Tool의 입력값을 확인합니다.
2. Tool 함수가 어떤 값을 반환하는지 봅니다.
3. 잘못된 입력이 들어왔을 때 처리 방식을 생각합니다.

## 실행 예제

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\01_function-calling-basic\01_simple-calculator-tool.py
```

## Tool 설계 표

| 항목 | 내용 |
| --- | --- |
| Tool 이름 | `add_numbers` |
| 입력값 | `a`, `b` |
| 출력값 | `{"result": 숫자}` |
| 실패 가능성 | 숫자가 아닌 값, 알 수 없는 함수 이름 |
| 대응 방법 | 입력 스키마 검증, 오류 JSON 반환 |

## 제출

- Tool 입력/출력 정의
- 실행 결과
- 예외 처리 아이디어
