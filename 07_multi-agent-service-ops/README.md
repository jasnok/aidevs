# 07_multi-agent-service-ops

`07_multi-agent-service-ops`는 05~06 과정에서 만든 Agent 코드를 실제 서비스처럼 실행하고 운영하는 방법을 배우는 과정입니다.

이 과정의 핵심은 하나의 작은 **Auto Healing Agent Service**를 기준으로 다음 흐름을 끝까지 연결하는 것입니다.

```text
Multi-Agent 협업 설계
-> Docker image 패키징
-> Docker Compose 로컬 운영
-> GitHub Actions 자동 검증
-> AWS ECR/App Runner 배포
-> CloudWatch Logs 확인
-> 보안/가드레일 적용
-> Auto Healing 장애 대응
-> 운영 대시보드와 실행 이력 관리
-> AWS 리소스 삭제와 비용 점검
```

## 과정 목표

| 영역 | 목표 |
| --- | --- |
| 멀티 에이전트 협업 설계 | 역할 기반 Agent 분리, Supervisor/Router, Handoff, Context 전달, Feedback Loop를 설계합니다. |
| 서비스 배포 및 자동화 운영 | Docker, Docker Compose, GitHub Actions, AWS ECR/App Runner, CloudWatch를 사용해 서비스를 배포하고 확인합니다. |
| AI 보안 및 가드레일 설계 | Prompt Injection, 정책 기반 응답 검증, Tool 권한 제어, Agent 접근 제어를 적용합니다. |
| 단위 프로젝트 | 에러 자가 치유(Auto Healing) 워크플로우를 구현하고 운영 결과를 검증합니다. |

## 전체 구조

```text
07_multi-agent-service-ops
├─ README.md
├─ SETUP.md
├─ .env.example
├─ requirements.txt
├─ 00_references
├─ 01_multi-agent-collaboration
├─ 02_service-deployment-and-automation
├─ 03_ai-security-and-guardrails
├─ 04_auto-healing-workflow
├─ 05_observability-and-ops-dashboard
├─ 90_ai-assisted-service-ops-review-and-debugging
└─ 99_final-service-ops-project
```

## 폴더 역할

| 폴더 | 역할 |
| --- | --- |
| `00_references` | 전체 운영 흐름, AWS 배포, 비용/삭제, 보안/관측성 기준을 정리합니다. |
| `01_multi-agent-collaboration` | Supervisor, Ops Agent, Security Agent, Recovery Agent 같은 역할 기반 협업 구조를 학습합니다. |
| `02_service-deployment-and-automation` | 간단한 FastAPI 서비스를 Docker, Compose, GitHub Actions, AWS로 전개합니다. |
| `03_ai-security-and-guardrails` | Prompt Injection 방어, 정책 검증, Tool 권한, Agent 접근 제어를 다룹니다. |
| `04_auto-healing-workflow` | 장애 감지, retry, restart, fallback, 복구 결과 검증 흐름을 학습합니다. |
| `05_observability-and-ops-dashboard` | 로컬 로그, Mock trace, CloudWatch Logs, 운영 대시보드 흐름을 연결합니다. |
| `90_ai-assisted-service-ops-review-and-debugging` | Docker, GitHub Actions, AWS, 보안, Auto Healing 오류를 AI와 함께 점검하는 가이드입니다. |
| `99_final-service-ops-project` | Auto Healing Agent Service 최종 프로젝트입니다. |

## 필수 실습 기준

07 과정에서 AWS 배포는 필수 실습입니다. 비용이 발생할 수 있으므로 예산 알림 설정, 실습 후 리소스 삭제, 비용 확인까지 필수 절차에 포함합니다.

필수로 확인해야 하는 항목:

- Docker image build/run
- Docker Compose 기반 backend/frontend/worker/monitor 실행
- GitHub Actions에서 Python 문법 검사, Compose config 검증, Docker build 검증
- AWS ECR repository 생성, image push
- AWS App Runner 배포
- 배포 URL의 `/health` 확인
- CloudWatch Logs 확인
- Prompt Injection, Tool 권한, Agent 접근 제어 기준 설명
- Auto Healing 장애 감지와 복구 흐름 검증
- AWS 리소스 삭제와 비용 점검

## 비용과 보안 주의

- OpenAI API, AWS 리소스는 비용이 발생할 수 있습니다.
- AWS Budget 또는 비용 알림을 설정합니다.
- AWS Access Key, OpenAI API Key, `.env` 파일은 GitHub에 올리지 않습니다.
- 실습 후 App Runner service, ECR image/repository, CloudWatch Log Group 등 사용한 리소스를 정리합니다.
- GitHub Actions에서 AWS에 연결할 때는 장기 Access Key보다 OIDC 기반 인증을 권장합니다. 수업에서는 먼저 Secret 기반 흐름을 이해하고, 운영 기준으로 OIDC를 설명합니다.

## 완료 기준

이 과정을 마치기 전에는 다음을 설명하거나 시연할 수 있어야 합니다.

1. Multi-Agent 역할 분리와 협업 흐름
2. Docker Compose로 여러 서비스를 함께 실행하는 방법
3. GitHub Actions 자동 검증 결과 확인
4. AWS ECR/App Runner 배포 흐름
5. CloudWatch Logs에서 실행 로그를 찾는 방법
6. Prompt Injection과 Tool 권한 제어 기준
7. Health Check, Retry, Restart, Fallback 기반 Auto Healing 흐름
8. AWS 리소스 삭제와 비용 확인 방법

## 진행 순서

1. [SETUP.md](./SETUP.md)를 보고 Python, Docker, GitHub, AWS 환경을 준비합니다.
2. [00_references](./00_references/README.md)에서 전체 서비스 운영 흐름을 확인합니다.
3. [01_multi-agent-collaboration](./01_multi-agent-collaboration/README.md)에서 역할 기반 Agent 협업 구조를 설계합니다.
4. [02_service-deployment-and-automation](./02_service-deployment-and-automation/README.md)에서 Docker, GitHub Actions, AWS 배포를 실습합니다.
5. [03_ai-security-and-guardrails](./03_ai-security-and-guardrails/README.md)에서 보안과 권한 제어를 적용합니다.
6. [04_auto-healing-workflow](./04_auto-healing-workflow/README.md)에서 장애 대응 흐름을 구현합니다.
7. [05_observability-and-ops-dashboard](./05_observability-and-ops-dashboard/README.md)에서 로그와 운영 대시보드를 확인합니다.
8. [99_final-service-ops-project](./99_final-service-ops-project/README.md)에서 최종 프로젝트를 완성합니다.
