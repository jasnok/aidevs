# 03_reasoning-and-react-basics

이 챕터에서는 LLM이 문제를 단계적으로 처리하는 흐름을 학습합니다.

## 핵심 개념

- Plan은 먼저 해결 순서를 정리하는 단계입니다.
- Act는 실제 행동 또는 도구 호출에 해당하는 단계입니다.
- Review는 결과를 검토하고 수정하는 단계입니다.
- ReAct는 Reasoning과 Action을 번갈아 사용하는 패턴입니다.
- 이 챕터에서는 실제 Tool을 호출하지 않고, Tool이 필요하다고 판단하는 흐름만 연습합니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\03_reasoning-and-react-basics\01_plan-act-review-pattern.py
python .\03_reasoning-and-react-basics\02_react-style-without-tools.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_plan-act-review-pattern.py` | 계획, 실행, 검토 항목으로 응답을 정리하는 예제입니다. |
| `02_react-style-without-tools.py` | 실제 도구 호출 전, 어떤 도구가 필요한지 판단하는 ReAct 스타일 예제입니다. |

## 주의할 점

이 단원에서는 모델의 숨겨진 내부 사고 과정을 길게 출력하게 만드는 것이 목표가 아닙니다. 수업에서는 사용자가 볼 수 있는 계획, 선택 이유, 최종 응답 형식을 중심으로 다룹니다.

## 확인 질문

- 바로 답변하는 것과 계획을 세운 뒤 답변하는 것은 무엇이 다른가요?
- ReAct에서 Action은 어떤 역할을 하나요?
- 실제 Tool 호출은 어느 단원에서 이어서 다루나요?
