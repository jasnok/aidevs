# 02 Prompt and Structured Output

## 학습 목표

- Role, Instruction, Context, Constraint를 구분해 Prompt를 작성합니다.
- 일반 dict/JSON과 Pydantic 검증의 차이를 설명합니다.
- 누락값, 잘못된 값, 계약에 없는 값을 명시적으로 처리합니다.
- 같은 Pydantic Schema로 Mock, Gemini, GPT, Ollama/Llama 결과를 비교합니다.

## 먼저 구분할 세 가지

```text
1. JSON/dict             데이터를 key-value 형태로 표현
2. Pydantic Validation   Python에서 타입·범위·필드 계약 검증
3. Structured Output     LLM에게 Schema에 맞는 응답 생성을 요청하고 다시 검증
```

JSON처럼 보이는 문자열이라고 해서 안전한 데이터는 아닙니다. Backend에서
Pydantic 검증을 통과해야 Tool, Database, Frontend로 전달할 수 있습니다.

## 학습 순서

1. `00_prompt_components.py`: Prompt의 네 구성 요소를 조립합니다.
2. `01_concept_example.py`: 일반 dict의 정상·오류·추가 필드를 검증합니다.
3. `02_travel_example.py`: LLM 출력이라고 가정한 여행 JSON을 검증합니다.
4. `03_real_provider_comparison.py`: Mini Agent 02 Backend로 Provider를 비교합니다.

## 실행

```powershell
python .\00_prompt_components.py
python .\01_concept_example.py
python .\02_travel_example.py
```

`03_real_provider_comparison.py`는 `C:\mini_agent_st\mini_agent_02_structured_output`
Backend를 먼저 실행한 뒤 사용합니다.

```powershell
python .\03_real_provider_comparison.py
```

기본 비교는 Mock으로 비용 없이 확인합니다. 그다음 이전 과정의 Gemini, OpenAI
GPT, Docker Ollama/Llama를 선택적으로 연결합니다. 한 Provider가 실패해도 다른
결과는 유지하여 설정 오류와 응답 차이를 함께 관찰합니다.

## Mini Agent 연결

```text
Prompt 구성 예제
→ Prompt 구성 메뉴
→ Pydantic 검증 예제
→ JSON 검증 메뉴
→ Structured Output API
→ Provider 비교 메뉴
```

## 완료 체크

- [ ] Prompt의 Role, Instruction, Context, Constraint를 설명할 수 있다.
- [ ] JSON 파싱 성공과 Schema 검증 성공이 다르다는 것을 설명할 수 있다.
- [ ] ValidationError에서 문제가 생긴 필드를 찾을 수 있다.
- [ ] LLM의 구조화 결과도 Backend에서 다시 검증해야 하는 이유를 설명할 수 있다.
