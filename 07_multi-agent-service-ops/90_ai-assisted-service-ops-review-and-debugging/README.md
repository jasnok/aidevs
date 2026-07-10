# 90_ai-assisted-service-ops-review-and-debugging

이 폴더는 07 과정에서 막히기 쉬운 운영 오류를 AI와 함께 점검하기 위한 가이드입니다.

Docker, GitHub Actions, AWS, 보안 가드레일, Auto Healing은 오류 메시지가 길고 원인이 여러 곳에 흩어지는 경우가 많습니다. Codex에게 질문할 때는 실행 명령, 로그, 기대 결과, 실제 결과를 함께 제공합니다.

## 문서 목록

| 파일 | 내용 |
| --- | --- |
| `01_docker-compose-troubleshooting.md` | Docker Compose, 포트, 컨테이너 로그 문제 |
| `02_github-actions-debugging.md` | GitHub Actions 실패 로그 분석 |
| `03_aws-deployment-and-cost-debugging.md` | ECR/App Runner/CloudWatch/비용 문제 |
| `04_security-guardrail-review.md` | Prompt Injection, Tool 권한, 정책 검증 점검 |
| `05_auto-healing-failure-review.md` | 장애 감지와 복구 실패 점검 |
| `06_final-ops-checklist.md` | 최종 운영 점검표 |

## Codex에게 줄 정보

```text
1. 어떤 명령을 실행했는가?
2. 어느 폴더에서 실행했는가?
3. 기대한 결과는 무엇인가?
4. 실제 출력 또는 오류 로그는 무엇인가?
5. 이미 확인한 내용은 무엇인가?
```

비밀값은 제거하고 공유합니다.

```text
OPENAI_API_KEY=***
AWS_SECRET_ACCESS_KEY=***
```
