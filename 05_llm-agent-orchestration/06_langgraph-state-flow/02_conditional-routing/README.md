# 02 Conditional Routing

이 폴더에서는 조건에 따라 Agent 실행 흐름을 다르게 보내는 방법을 학습합니다.

## 핵심 개념

- Conditional Routing은 State 값을 보고 다음 Node를 선택합니다.
- Retry는 실패 후 다시 시도하는 흐름입니다.
- Self-Reflection은 Agent가 자신의 결과를 점검하고 개선하는 단계입니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_conditional-route-basic.py` | 조건값에 따라 다음 Node를 선택하는 기본 예제 |
| `02_retry-and-reflection-flow.py` | 오류를 감지하고 수정한 뒤 다시 시도하는 예제 |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow
.\.venv\Scripts\Activate.ps1
python .\02_conditional-routing\01_conditional-route-basic.py
python .\02_conditional-routing\02_retry-and-reflection-flow.py
```

## 확인 질문

- 조건 분기가 없으면 Agent 흐름에 어떤 한계가 생기는가?
- Retry 횟수는 왜 제한해야 하는가?
- Self-Reflection은 어떤 기준으로 성공과 실패를 판단해야 하는가?
