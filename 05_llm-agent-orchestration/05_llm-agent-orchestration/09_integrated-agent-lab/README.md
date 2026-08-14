# 09 Integrated Agent Lab

01~08에서 단계적으로 완성한 여행 Agent를 한 번에 실행하고 전체 데이터 흐름을 설명하는 최종 실습입니다. Backend와 Frontend 코드를 다시 복사하지 않고 다음 누적 완성본을 사용합니다.

```text
C:\mini_agent_st\mini_agent_08_evaluation
├─ backend_python
├─ backend_langgraph
├─ frontend
├─ learning_unit
└─ steps
```

## 실행

처음 한 번만 환경을 준비합니다.

```powershell
cd C:\mini_agent_st\mini_agent_08_evaluation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

터미널 1:

```powershell
cd C:\mini_agent_st\mini_agent_08_evaluation\backend_python
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
```

터미널 2:

```powershell
cd C:\mini_agent_st\mini_agent_08_evaluation\backend_langgraph
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8001
```

터미널 3:

```powershell
cd C:\mini_agent_st\mini_agent_08_evaluation
.\.venv\Scripts\python.exe -m streamlit run .\frontend\app.py
```

## 최종 확인 순서

1. 두 Backend의 `/health`와 `/docs`를 확인합니다.
2. Streamlit에서 Python과 LangGraph Backend를 각각 선택합니다.
3. 정상 요청과 정보 부족 요청을 실행합니다.
4. Tool·RAG·Memory 결과를 확인합니다.
5. Mock 예약 요청을 승인하고, 새 요청은 거절합니다.
6. 다른 사용자 승인과 중복 승인이 차단되는지 확인합니다.
7. 기본 평가 시나리오와 Trace를 실행합니다.
8. 기준 결과를 저장하고 회귀 테스트를 실행합니다.

## 필수 확장

- 허용된 Mock Tool 하나 추가
- 정책 문서 하나 추가
- 정상 시나리오와 실패 시나리오 각각 하나 추가
- 추가한 기능의 Trace에서 실행 순서 설명

확장 전후에는 [최종 리뷰와 디버깅 체크리스트](./review-checklist.md)로 권한·근거·Trace·회귀 여부를 점검합니다.

## 제외 범위

- 실제 예약·결제·환불
- LLM Judge와 외부 평가 플랫폼
- Docker Compose와 AWS 배포
- Multi-Agent

Docker Compose와 AWS EC2 배포는 후속 운영 과정에서 진행합니다.

## 완료 기준

```text
Streamlit 입력
→ FastAPI 요청 검증
→ Python 또는 LangGraph Agent
→ Tool·RAG·Memory
→ 승인과 안전 실행
→ 평가와 Trace
→ Streamlit 결과
```

이 흐름을 코드와 화면으로 설명하고, 기능 하나를 추가한 뒤 기존 시나리오에 회귀가 없는지 확인하면 완료입니다.
