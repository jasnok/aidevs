# 03_openai-vs-llama-comparison

이 챕터에서는 같은 질문을 OpenAI 모델과 로컬 Llama 모델에 보내고 응답 차이를 비교합니다.

## 핵심 개념

- OpenAI 기본 모델은 `gpt-4.1-mini`입니다.
- Llama는 Docker/Ollama로 실행하는 로컬 모델입니다.
- 모델별로 응답 속도, 문체, 정확도, 비용 구조가 달라질 수 있습니다.
- OpenAI API Key가 없으면 OpenAI 호출은 건너뛰고 Llama 결과만 비교할 수 있습니다.

## 실행 전 확인

```powershell
docker ps
docker exec -it ollama-llm ollama list
```

OpenAI까지 함께 비교하려면 `.env`의 `OPENAI_API_KEY`도 실제 값으로 설정되어 있어야 합니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm
.\.venv\Scripts\Activate.ps1
python .\03_openai-vs-llama-comparison\01_compare-basic-answer.py
python .\03_openai-vs-llama-comparison\02_compare-prompt-style.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_compare-basic-answer.py` | 같은 질문을 두 모델에 보내고 응답과 소요 시간을 비교합니다. |
| `02_compare-prompt-style.py` | 출력 형식을 지정했을 때 두 모델이 형식을 얼마나 잘 지키는지 비교합니다. |

## 기록할 내용

- 두 모델의 응답 길이
- 두 모델의 설명 방식
- 더 이해하기 쉬웠던 응답
- 실습 프로젝트에서 어떤 모델을 우선 사용할지에 대한 이유

## 비교 표 예시

| 기준 | OpenAI `gpt-4.1-mini` | 로컬 Llama |
| --- | --- | --- |
| 응답 속도 |  |  |
| 설명 품질 |  |  |
| 출력 형식 준수 |  |  |
| 비용/자원 |  |  |
| 프로젝트 적용 의견 |  |  |
