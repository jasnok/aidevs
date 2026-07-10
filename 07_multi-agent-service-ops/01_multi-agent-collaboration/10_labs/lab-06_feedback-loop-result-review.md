# Lab 06. Feedback Loop Result Review

## 목표

Agent 실행 결과를 검증하고, 기준을 통과하지 못하면 재시도 또는 fallback하는 흐름을 설계합니다.

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\01_multi-agent-collaboration
python .\06_feedback-loop-result-review\01_feedback_loop_result_review.py
```

## 작성할 내용

1. 검증 기준
2. 실패 유형
3. 재시도 조건
4. 최대 재시도 횟수
5. 반복 실패 시 fallback
6. 로그에 남길 정보

## 확인 질문

- 재시도를 무한히 하면 어떤 문제가 생기는가?
- 검증은 LLM이 해야 하는가, 규칙 기반 코드가 해야 하는가?
- 실패 응답과 재시도 결과를 운영 대시보드에 어떻게 보여줄 것인가?
