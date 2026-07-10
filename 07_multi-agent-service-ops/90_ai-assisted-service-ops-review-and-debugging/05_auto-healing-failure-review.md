# 05 Auto Healing Failure Review

## 확인할 흐름

```text
장애 감지
-> 장애 유형 분류
-> 복구 action 선택
-> retry/restart/fallback 실행
-> health check 재확인
-> 결과 로그 기록
```

## 자주 보는 문제

| 증상 | 확인할 것 |
| --- | --- |
| 장애를 감지하지 못함 | health check 조건, timeout, 로그 수집 |
| 잘못된 복구 action 선택 | 장애 유형 분류 기준 |
| retry가 무한 반복됨 | retry limit |
| restart 후에도 실패 | 실제 원인이 config/env/권한인지 확인 |
| fallback 메시지가 없음 | 사용자에게 안내할 최종 응답 |
| 복구 결과가 기록되지 않음 | event log와 status field |

## Codex 질문 예시

```text
Auto Healing 파이프라인이 retry만 반복하고 종료하지 않습니다.
장애 메시지:
...
현재 state:
...
복구 정책:
...
어디에 종료 조건을 넣어야 하는지 알려줘.
```
