# Lab 02. JSON Output Check

## 목표

LLM 응답을 JSON 형식으로 받고, 프로그램에서 사용 가능한 구조인지 확인합니다.

## 진행

1. JSON 출력 요청 프롬프트를 작성합니다.
2. 필수 필드를 정합니다.
3. 예제를 실행합니다.
4. 누락된 필드나 타입 오류가 있는지 확인합니다.

## 실행 예제

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\02_structured-output-json\01_json-output-request.py
python .\02_structured-output-json\02_structured-output-pydantic.py
```

## 확인할 구조

```json
{
  "summary": "한 문장 요약",
  "sentiment": "positive | neutral | negative",
  "keywords": ["키워드1", "키워드2"],
  "difficulty": 1
}
```

## 비교 기준

- JSON으로 파싱 가능한가?
- 필수 필드가 빠지지 않았는가?
- 숫자 필드는 숫자로 들어왔는가?
- Pydantic 모델을 적용했을 때 코드에서 더 다루기 쉬운가?

## 제출

- 요청한 JSON 구조
- 실제 응답
- 개선할 점
- Pydantic 검증이 필요한 이유
