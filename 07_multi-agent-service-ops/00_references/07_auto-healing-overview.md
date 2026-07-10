# 07. Auto Healing Overview

Auto Healing은 장애를 감지하고 가능한 경우 자동으로 복구하는 흐름입니다.

## 기본 흐름

```text
장애 감지
-> 장애 유형 분류
-> 복구 전략 선택
-> retry/restart/fallback 실행
-> 복구 결과 검증
-> 이벤트 로그 기록
```

## 장애 유형 예시

| 장애 유형 | 예시 | 대응 |
| --- | --- | --- |
| unhealthy | `/health` 실패 | 재시작 또는 점검 |
| timeout | 응답 지연 | retry 또는 timeout 조정 |
| api_error | 외부 API 5xx | 재시도 또는 fallback |
| rate_limit | 호출량 초과 | 대기 후 재시도 |
| permission_error | 권한 부족 | 설정 또는 Secret 확인 |
| prompt_error | Prompt Injection 또는 응답 정책 위반 | 입력 차단 또는 응답 필터링 |

## 중요한 기준

- 무한 재시도는 금지합니다.
- 최대 재시도 횟수를 정합니다.
- 실패 이유를 로그로 남깁니다.
- 복구 후 반드시 결과를 검증합니다.
- 자동 복구가 어려우면 사람이 확인할 수 있게 상태를 표시합니다.
