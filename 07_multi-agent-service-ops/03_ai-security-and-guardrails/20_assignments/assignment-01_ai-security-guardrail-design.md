# Assignment 01. AI Security Guardrail Design

## 과제 목표

팀 미니 프로젝트에 적용할 AI 보안과 가드레일 구조를 설계합니다.

## 필수 작성 내용

1. Prompt Injection 방어 기준
2. 입력 검증 규칙
3. 출력 검증 정책
4. Agent 역할별 Tool 권한 표
5. Agent 역할별 데이터 접근 권한 표
6. 차단/수정/허용 로그에 남길 정보
7. Docker/AWS 운영 환경에서 관리할 Secret 목록

## 제출 형식

Markdown 문서로 제출합니다.

```text
team-name_ai-security-guardrail-design.md
```

## 평가 기준

- 위험 입력과 정상 입력을 구분하려는 기준이 있는가?
- Tool 권한이 최소 권한 원칙에 맞게 설계되었는가?
- 정책 위반 응답을 어떻게 처리할지 설명되어 있는가?
- 운영 로그와 Secret 관리 관점이 포함되어 있는가?
