# Lab 03. Multi Tool Selection

## 목표

사용자 요청에 따라 여러 Tool 중 하나를 선택하는 기준을 설계합니다.

## 진행

1. Tool 목록을 작성합니다.
2. 각 Tool이 처리할 수 있는 요청 유형을 정합니다.
3. Router 조건을 설계합니다.
4. 잘못 선택했을 때의 Fallback을 작성합니다.

## 실행 예제

```powershell
cd C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use
.\.venv\Scripts\Activate.ps1
python .\03_multi-tool-orchestration\01_multi-tool-router.py
python .\03_multi-tool-orchestration\02_manual-tool-selection-flow.py
```

## 선택 기준 표

| 사용자 요청 유형 | 선택할 Tool | 이유 |
| --- | --- | --- |
| 로그 조회 | `get_learning_logs` | 원본 로그 목록이 필요함 |
| 총 시간 계산 | `calculate_total_minutes` | 숫자 계산은 Tool이 정확함 |
| 다음 주제 추천 | `recommend_next_topic` | 현재 주제 기반 추천 필요 |
| 날씨 조회 | `get_mock_weather` | 외부 정보 조회에 해당 |
| 불명확한 요청 | `none` 또는 clarification | 추가 질문이 필요함 |

## 제출

- Tool 목록
- 선택 조건
- Fallback 전략
- Tool 결과가 부족할 때의 다음 행동
