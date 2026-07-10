# Worker

백그라운드 Auto Healing 작업을 처리하는 영역입니다.

## 역할

- 장애 이벤트 처리
- Agent 실행
- retry/restart/fallback 전략 실행
- 복구 결과 기록

## 확인할 것

- 작업 로그가 남는가?
- 실패 시 재시도 횟수가 제한되는가?
- 복구 결과가 monitor에서 확인 가능한가?
