# Backend

FastAPI 기반 API 서버 영역입니다.

## 역할

- `/health` endpoint 제공
- Auto Healing 요청 접수
- Agent 실행 상태 제공
- 이벤트 로그 조회 API 제공

## 확인할 것

- health check가 정상 응답하는가?
- worker와 공유할 데이터 형식이 명확한가?
- 오류 응답 형식이 일관적인가?
