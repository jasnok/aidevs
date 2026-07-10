# Lab 07. Guardrails AI Integrated Validation

## 목표

Guardrails AI 같은 검증 도구를 AI 서비스 흐름의 어디에 붙일지 설계합니다.

## 검증 위치

```text
사용자 입력
-> 입력 검증
-> Agent 실행
-> Tool 권한 확인
-> 응답 검증
-> 감사 로그 기록
```

## 작성할 내용

- 입력 검증에 사용할 규칙
- 응답 검증에 사용할 규칙
- 정책 위반 시 fallback 응답
- Guardrails 도구를 붙일 위치
- 검증 실패 로그 구조

## 확인 질문

- 모든 검증을 LLM에게 맡기면 어떤 문제가 생기는가?
- 규칙 기반 검증과 모델 기반 검증은 어떻게 나누면 좋은가?
