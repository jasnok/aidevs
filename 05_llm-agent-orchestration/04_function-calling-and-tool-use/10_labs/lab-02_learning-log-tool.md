# Lab 02. Learning Log Tool

## 목표

학습 로그를 요약하는 Tool을 설계하고 Agent가 사용할 수 있는 형태로 정리합니다.

## 진행

1. 학습 로그 데이터 예시를 확인합니다.
2. 요약 기준을 정합니다.
3. Tool 실행 결과를 확인합니다.
4. 최종 응답에 어떤 정보가 필요한지 정리합니다.

## 실행 예제

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\01_function-calling-basic\02_learning-log-summary-tool.py
```

## Tool 설계 표

| 항목 | 내용 |
| --- | --- |
| Tool 이름 | `get_learning_logs` |
| 입력값 | `learner` |
| 출력값 | 학습 로그 목록 |
| 최종 응답에 필요한 정보 | 총 학습 시간, 진행 중인 주제, 완료한 주제 |
| 실패 가능성 | 학습자 이름 없음, 로그 없음 |

## 제출

- 로그 데이터 구조
- 요약 기준
- Tool 결과 예시
- 로그가 없을 때의 응답 전략
