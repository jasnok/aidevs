# Lab 01. Improve Basic Prompt

## 목표

역할, 지시문, 맥락을 나누어 프롬프트 품질을 개선합니다.

## 진행

1. 같은 질문을 단순 프롬프트로 작성합니다.
2. Role, Instruction, Context를 나누어 다시 작성합니다.
3. 두 응답을 비교합니다.

## 실행 예제

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\01_prompt-design-patterns\01_role-and-context-prompt.py
python .\01_prompt-design-patterns\02_few-shot-style-prompt.py
```

## 비교 기준

| 기준 | 개선 전 | 개선 후 |
| --- | --- | --- |
| 역할이 명확한가 |  |  |
| 지시문이 구체적인가 |  |  |
| 맥락이 충분한가 |  |  |
| 출력 형식이 안정적인가 |  |  |
| 바로 수업/서비스에 사용할 수 있는가 |  |  |

## 제출

- 개선 전 프롬프트
- 개선 후 프롬프트
- 응답 차이 분석
- 개선 후 프롬프트가 더 나은 이유
