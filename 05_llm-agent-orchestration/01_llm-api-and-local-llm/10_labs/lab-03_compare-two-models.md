# Lab 03. Compare Two Models

## 목표

OpenAI `gpt-4.1-mini`와 로컬 Llama의 응답을 비교합니다.

이 실습은 “어떤 모델이 무조건 더 좋다”를 고르는 활동이 아닙니다. 같은 질문이라도 모델 실행 위치, 비용 구조, 응답 스타일, 출력 형식 준수 정도가 다를 수 있음을 확인하는 활동입니다.

## 진행

1. OpenAI API Key가 있다면 `.env`에 입력합니다.
2. Ollama/Llama 컨테이너를 실행합니다.
3. `01_compare-basic-answer.py`를 실행합니다.
4. `02_compare-prompt-style.py`를 실행합니다.
5. 결과를 표로 정리합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
python .\03_openai-vs-llama-comparison\01_compare-basic-answer.py
python .\03_openai-vs-llama-comparison\02_compare-prompt-style.py
```

OpenAI API Key가 없다면 OpenAI 결과는 건너뛰고 Llama 결과만 기록합니다.

## 비교 기준

- 응답 속도
- 문체
- 정확도
- 비용 또는 실행 자원
- 수업용 예제로 적합한 정도

## 기록 표

| 기준 | OpenAI `gpt-4.1-mini` | 로컬 Llama |
| --- | --- | --- |
| 응답 속도 |  |  |
| 설명 방식 |  |  |
| 출력 형식 준수 |  |  |
| 비용/자원 |  |  |
| 장점 |  |  |
| 주의점 |  |  |

## 정리 질문

- 이후 Agent 실습에서는 어떤 모델을 기본으로 쓰면 좋을까요?
- 로컬 모델을 사용하면 좋은 상황은 언제일까요?
- 클라우드 모델을 사용하면 좋은 상황은 언제일까요?
