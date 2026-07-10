# 02_structured-output-json

이 챕터에서는 LLM 응답을 JSON과 Pydantic 구조로 안정화하는 방법을 학습합니다.

## 핵심 개념

- 자유 문장 응답은 프로그램에서 처리하기 어렵습니다.
- JSON 응답은 필드 이름과 값의 구조를 맞추는 데 유리합니다.
- Pydantic은 응답 데이터의 타입과 필수 필드를 검증합니다.
- Structured Output은 이후 API 응답, Tool 결과, Agent 상태 관리의 기반이 됩니다.

## 실행 순서

```powershell
cd C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality
.\.venv\Scripts\Activate.ps1
python .\02_structured-output-json\01_json-output-request.py
python .\02_structured-output-json\02_structured-output-pydantic.py
```

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `01_json-output-request.py` | 프롬프트로 JSON 형식 응답을 요청하고 `json.loads()`로 파싱을 시도합니다. |
| `02_structured-output-pydantic.py` | Pydantic 모델을 사용해 응답 구조를 더 엄격하게 검증합니다. |

## 관찰할 내용

- 모델이 JSON만 출력했는가?
- 필수 필드가 모두 있는가?
- `difficulty` 같은 숫자 필드가 문자열이 아니라 숫자로 들어왔는가?
- Pydantic 모델을 쓰면 어떤 점이 더 명확해지는가?

## 확인 질문

- JSON 형식 응답이 필요한 이유는 무엇인가요?
- Pydantic 검증이 없으면 어떤 문제가 생길 수 있나요?
- 이후 FastAPI나 Agent Tool 결과와 어떻게 연결될 수 있나요?
