# 06 Feedback Loop Result Review

이 실습은 Agent 실행 결과를 검증하고, 기준을 통과하지 못하면 재시도 또는 fallback하는 Feedback Loop를 다룹니다.

## 기본 흐름

```text
Agent 실행
-> 결과 검증
-> 기준 통과 여부 확인
-> 실패하면 원인 기록
-> 재시도 또는 fallback
-> 최종 결과 생성
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\06_feedback-loop-result-review\01_feedback_loop_result_review.py
```

## 검증 기준 예시

| 기준 | 설명 |
| --- | --- |
| 필수 필드 존재 | 결과에 필요한 값이 모두 있는지 확인 |
| 정책 위반 없음 | 보안 정책을 위반하지 않았는지 확인 |
| Tool 결과와 응답 일치 | Tool 결과와 최종 응답이 다르지 않은지 확인 |
| 재시도 횟수 제한 | 무한 반복을 막기 위해 최대 횟수를 둠 |

## 운영 연결

Feedback Loop 결과는 05 단원의 로그/trace와 04 단원의 Auto Healing 흐름으로 이어집니다.
