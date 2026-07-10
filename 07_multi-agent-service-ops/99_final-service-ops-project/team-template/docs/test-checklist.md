# Test Checklist

## 실행 확인

- [ ] `Copy-Item .env.example .env` 실행
- [ ] `docker compose config` 성공
- [ ] `docker compose up --build` 성공
- [ ] backend `/health` 정상 응답
- [ ] frontend 접속 가능
- [ ] monitor 접속 가능

## Multi-Agent 확인

- [ ] Supervisor Agent 역할 정의
- [ ] Diagnosis Agent 역할 정의
- [ ] Recovery Agent 역할 정의
- [ ] Validation Agent 역할 정의
- [ ] Agent 간 Context 전달 기준 작성

## Auto Healing 확인

- [ ] 장애 유형 2개 이상 정의
- [ ] retry/restart/fallback 기준 작성
- [ ] 복구 결과 검증 기준 작성
- [ ] 실패 이벤트 로그 추가

## 운영 확인

- [ ] 보안 정책 점검
- [ ] 권한 위반 로그 기준 작성
- [ ] dashboard 표시 항목 정리
- [ ] AWS 배포 체크리스트 작성
