# 11 Course Alignment Checklist

이 문서는 07 과정의 커리큘럼 요구사항이 현재 폴더에 어디에 반영되어 있는지 확인하는 체크리스트입니다.

## 멀티 에이전트 협업 설계

| 요구사항 | 위치 | 확인 |
| --- | --- | --- |
| 단일 Agent와 Multi-Agent 구조 비교 | `01_multi-agent-collaboration/01_single-vs-multi-agent` | [ ] |
| 역할 기반 Agent 분리 | `01_multi-agent-collaboration/02_role-based-agent-design` | [ ] |
| Supervisor/Router 기반 작업 분배 | `01_multi-agent-collaboration/03_supervisor-router-workflow` | [ ] |
| 분산 협업 구조와 결과 통합 | `01_multi-agent-collaboration/04_distributed-agent-collaboration` | [ ] |
| Handoff와 Context 공유, MCP 개념 | `01_multi-agent-collaboration/05_handoff-context-mcp` | [ ] |
| 실행 결과 검증과 Feedback Loop | `01_multi-agent-collaboration/06_feedback-loop-result-review` | [ ] |

## 서비스 배포 및 자동화 운영

| 요구사항 | 위치 | 확인 |
| --- | --- | --- |
| Docker 기반 서비스 패키징 | `02_service-deployment-and-automation/01_docker-service-packaging` | [ ] |
| Docker Compose 기반 멀티 서비스 실행 | `02_service-deployment-and-automation/02_docker-compose-multi-service` | [ ] |
| Health Check와 Runtime 로그 확인 | `02_service-deployment-and-automation/03_service-health-and-runtime` | [ ] |
| GitHub Actions 기반 CI/CD 검증 | `02_service-deployment-and-automation/04_github-actions-cicd` | [ ] |
| AWS ECR/App Runner 배포 | `02_service-deployment-and-automation/05_aws-deployment-basic` | [ ] |
| AWS 리소스 삭제와 비용 점검 | `02_service-deployment-and-automation/06_aws-cleanup-and-cost-control` | [ ] |

## AI 보안 및 가드레일 설계

| 요구사항 | 위치 | 확인 |
| --- | --- | --- |
| Prompt Injection 방어 | `03_ai-security-and-guardrails/01_prompt-injection-defense` | [ ] |
| 정책 기반 응답 검증 | `03_ai-security-and-guardrails/02_policy-based-response-validation` | [ ] |
| Tool 실행 권한 제어 | `03_ai-security-and-guardrails/03_tool-permission-control` | [ ] |
| Multi-Agent 접근 제어 | `03_ai-security-and-guardrails/04_multi-agent-access-control` | [ ] |
| 감사 로그와 정책 위반 추적 | `03_ai-security-and-guardrails/10_labs/lab-06_audit-log-policy-violation.md` | [ ] |
| Guardrails 통합 검증 | `03_ai-security-and-guardrails/10_labs/lab-07_guardrails-ai-integrated-validation.md` | [ ] |

## Auto Healing 및 관측성

| 요구사항 | 위치 | 확인 |
| --- | --- | --- |
| 장애 유형 분류 | `04_auto-healing-workflow/01_failure-scenarios` | [ ] |
| Health Check, Retry, Restart | `04_auto-healing-workflow/02_health-check-retry-restart` | [ ] |
| 복구 파이프라인 | `04_auto-healing-workflow/03_recovery-pipeline` | [ ] |
| 복구 결과 검증 | `04_auto-healing-workflow/04_recovery-result-validation` | [ ] |
| 로컬 로그와 실행 이력 | `05_observability-and-ops-dashboard/01_logging-and-event-history` | [ ] |
| Trace와 LangSmith 개념 | `05_observability-and-ops-dashboard/02_tracing-and-monitoring` | [ ] |
| 운영 대시보드 | `05_observability-and-ops-dashboard/03_ops-dashboard-streamlit` | [ ] |
| CloudWatch Logs 확인 | `05_observability-and-ops-dashboard/05_cloudwatch-log-review` | [ ] |

## 최종 프로젝트

| 요구사항 | 위치 | 확인 |
| --- | --- | --- |
| 에러 자가 치유(Auto Healing) 워크플로우 | `99_final-service-ops-project` | [ ] |
| Docker Compose 실행 결과 | `99_final-service-ops-project/project-deliverables` | [ ] |
| GitHub Actions 실행 결과 | `99_final-service-ops-project/project-deliverables` | [ ] |
| AWS 배포 결과 | `99_final-service-ops-project/project-deliverables` | [ ] |
| CloudWatch Logs 확인 결과 | `99_final-service-ops-project/project-deliverables` | [ ] |
| AWS 리소스 삭제 체크리스트 | `99_final-service-ops-project/project-deliverables` | [ ] |
