# Project Docs

팀 프로젝트 문서는 이 폴더에 정리합니다.

## 작성할 문서

| 문서 | 내용 |
| --- | --- |
| architecture.md | Multi-Agent 구조, 서비스 구성, Docker Compose 구조 |
| recovery-plan.md | 장애 유형, 복구 전략, 검증 기준 |
| security-guardrails.md | Prompt Injection, 정책 검증, Tool 권한 |
| observability.md | 로그, trace, dashboard 지표 |
| test-checklist.md | 실행과 검증 체크리스트 |

## 작성 기준

- 코드가 어떻게 동작하는지보다 운영자가 무엇을 확인할 수 있는지 설명합니다.
- 장애와 복구는 전후 상태를 비교합니다.
- 보안 정책과 권한 위반은 로그로 추적할 수 있어야 합니다.
