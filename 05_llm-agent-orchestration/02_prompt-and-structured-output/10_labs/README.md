# 02 Labs

## 실행 위치

Lab 1~3은 과정 폴더의 Python 파일만 사용하므로 Backend가 필요하지 않습니다.
Lab 4의 실제 Provider 비교는 다음 Backend를 먼저 실행합니다.

```powershell
cd C:\mini_agent_st\mini_agent_02_structured_output\backend
uvicorn app.main:app --reload --port 8000
```

Backend 실행 후 `02_prompt-and-structured-output\03_real_provider_comparison.py`를
실행하거나 같은 Mini의 Frontend에서 비교 결과를 확인합니다.

## Lab 1. Prompt 네 부분 만들기

여행 예약 취소 요청을 위한 Role, Instruction, Context, Constraint를 각각 작성하고
`00_prompt_components.py`의 `build_prompt()`로 조립하세요.

## Lab 2. 여행 요청 Schema 확장

`TravelRequest`에 다음 필드를 추가하세요.

- `children`: 0명 이상
- `allergies`: 문자열 목록
- `accommodation_preference`: `hotel`, `guesthouse`, `resort`, `unknown`

정상 예제와 필드가 누락된 예제를 각각 한 개 추가합니다.

## Lab 3. 검증 실패를 사용자 문장으로 바꾸기

다음 입력을 검증하고 Pydantic의 기술적인 오류를 사용자가 이해할 수 있는 한국어
문장으로 변환하세요.

- 성인 0명
- 문자열 예산
- 0박
- 허용하지 않은 이동 수단
- Schema에 없는 필드

예: `nights: Input should be greater than or equal to 1`을
`여행 일수는 1박 이상 입력해 주세요.`로 변환합니다.

## Lab 4. Mock과 실제 Provider 비교

Mini Agent 02의 Structured Output 비교 메뉴에서 같은 요청을 실행하고 다음을
기록하세요.

- 모든 결과가 같은 필드를 가지는가?
- 내용은 어떻게 다른가?
- 실패한 Provider가 있어도 다른 결과가 남는가?
