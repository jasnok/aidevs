# 99_final-service-ops-project

이 폴더는 07 과정의 최종 프로젝트 공간입니다.

주제:

```text
에러 자가 치유(Auto Healing) 워크플로우
```

프로젝트 목표는 Multi-Agent 협업 구조, Docker Compose 로컬 실행, GitHub Actions 자동 검증, AWS ECR/App Runner 배포, CloudWatch Logs 확인, 보안/가드레일, Auto Healing 결과 검증을 하나로 연결하는 것입니다.

## 구조

```text
99_final-service-ops-project
├─ README.md
├─ sample-auto-healing-agent
├─ team-template
└─ project-deliverables
```

## 폴더 역할

| 폴더 | 역할 |
| --- | --- |
| `sample-auto-healing-agent` | 수업 중 실행해 보는 완성형 작은 예제입니다. |
| `team-template` | 팀별 최종 프로젝트를 시작할 때 복사해서 사용하는 starter입니다. |
| `project-deliverables` | 필수 산출물 샘플과 체크리스트입니다. |

## 필수 산출물

| 산출물 | 설명 |
| --- | --- |
| Multi-Agent 협업 구조 설계서 | Supervisor, Ops, Security, Recovery Agent 역할과 Handoff 흐름 |
| Docker Compose 실행 결과 | backend/frontend/worker/monitor 실행 결과 |
| GitHub Actions 실행 결과 | Python, Compose, Docker build 자동 검증 결과 |
| AWS 배포 결과 보고서 | ECR image push, App Runner 배포 URL, `/health` 확인 |
| CloudWatch Logs 확인 결과 | Log Group, Log Stream, 주요 로그 |
| Auto Healing 장애 대응 결과 보고서 | 장애 유형, 복구 action, 결과 검증 |
| 보안/가드레일 정책 문서 | Prompt Injection, Tool 권한, Agent 접근 제어 |
| AWS 리소스 삭제 체크리스트 | App Runner, ECR, CloudWatch, 비용 확인 |

## 진행 순서

1. `sample-auto-healing-agent`를 실행해 전체 흐름을 확인합니다.
2. `team-template`을 복사해 팀 프로젝트를 시작합니다.
3. Docker Compose로 로컬 실행을 확인합니다.
4. GitHub Actions 자동 검증을 연결합니다.
5. AWS ECR/App Runner에 배포합니다.
6. CloudWatch Logs를 확인합니다.
7. 장애 시나리오와 Auto Healing 결과를 검증합니다.
8. AWS 리소스를 삭제하고 비용을 확인합니다.
9. `project-deliverables` 기준으로 최종 산출물을 정리합니다.
