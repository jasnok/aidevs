# Auto Healing 장애 대응 결과 보고서 샘플

## 장애 시나리오

| 시나리오 | 입력 메시지 | 기대 action | 실제 action | 결과 |
| --- | --- | --- | --- | --- |
| health check 실패 | backend health check failed | restart |  |  |
| API timeout | upstream timeout | retry |  |  |
| 권한 오류 | permission denied | escalate |  |  |
| 정책 위반 | prompt injection detected | block |  |  |

## 복구 흐름

```text
장애 감지
-> 장애 유형 분류
-> 복구 action 선택
-> 실행 또는 fallback
-> 결과 검증
-> event log 기록
```

## 결과 지표

| 지표 | 값 |
| --- | --- |
| 성공한 복구 수 |  |
| 실패한 복구 수 |  |
| fallback 수 |  |
| 평균 재시도 횟수 |  |
| 최종 상태 |  |

## 개선 사항

- 
