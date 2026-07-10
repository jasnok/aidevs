# Test Checklist

## 실행 확인

- [ ] `Copy-Item .env.example .env` 실행
- [ ] `docker compose config` 성공
- [ ] `docker compose up --build` 성공
- [ ] backend `/health` 정상 응답
- [ ] frontend 접속 가능
- [ ] monitor 접속 가능

## 기능 확인

- [ ] Auto Healing 요청 생성
- [ ] worker 작업 로그 확인
- [ ] 이벤트 이력 표시 확인
- [ ] 실패 이벤트 추가
- [ ] 복구 이벤트 추가
- [ ] dashboard 지표 변경 확인

## 운영 확인

- [ ] 장애 유형 분류 기준 작성
- [ ] retry/restart/fallback 기준 작성
- [ ] 보안 정책 점검
- [ ] AWS 배포 체크리스트 작성
