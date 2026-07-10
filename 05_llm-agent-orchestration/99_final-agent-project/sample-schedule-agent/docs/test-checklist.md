# Test Checklist

샘플 일정 조정 Agent 실행 전후에 확인할 항목입니다.

## 실행 전 준비

- [ ] 현재 폴더가 `sample-schedule-agent`인지 확인했습니다.
- [ ] `.venv`를 만들고 활성화했습니다.
- [ ] `python -m pip install --upgrade pip`를 실행했습니다.
- [ ] `pip install -r requirements.txt`를 실행했습니다.
- [ ] `.env.example`을 `.env`로 복사했습니다.
- [ ] OpenAI API Key가 필요한 경우 `.env`에 값을 입력했습니다.

## CLI 테스트

- [ ] `python -m app.graph`가 실행됩니다.
- [ ] State 값이 단계별로 업데이트됩니다.
- [ ] Tool 함수 결과가 출력됩니다.
- [ ] 최종 메시지가 생성됩니다.
- [ ] API Key가 없을 때도 규칙 기반 대체 흐름을 확인했습니다.

## UI 테스트

- [ ] `streamlit run .\frontend\streamlit_app.py --server.port 8601`가 실행됩니다.
- [ ] 입력창에 요청을 넣을 수 있습니다.
- [ ] 결과 메시지가 화면에 표시됩니다.
- [ ] 오류 메시지가 이해 가능한 형태로 표시됩니다.

## 개선 메모

- 실패한 테스트:
- 원인:
- 수정 방향:
