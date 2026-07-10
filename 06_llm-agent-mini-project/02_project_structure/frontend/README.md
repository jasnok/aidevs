# Frontend

이 폴더는 Streamlit 기반 Agent UI starter입니다.

## 역할

- 사용자의 일정 요청 입력
- backend `/agent/schedule` 호출
- Agent 응답, Tool 호출 이력, 오류 횟수 표시

## 실행 예시

```powershell
cd C:\aidev\06_llm-agent-mini-project\team-schedule-agent\frontend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## 구현할 내용

- backend 주소 입력 또는 `.env` 처리
- 일정 요청 입력창
- Agent 실행 버튼
- 결과 출력 영역
- Tool 호출 이력 표시
- 오류 또는 fallback 메시지 표시
