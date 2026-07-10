# 05 AWS Deployment Map

07 과정에서 AWS 배포는 필수 실습입니다. 단, 비용이 발생할 수 있으므로 배포 전 비용 안전장치를 설정하고, 실습 후 리소스를 삭제합니다.

## 기본 배포 흐름

```text
로컬 FastAPI /health 확인
-> Docker image build
-> Docker image run
-> ECR repository 생성
-> ECR login
-> image tag
-> image push
-> App Runner에서 ECR image 배포
-> 배포 URL /health 확인
-> CloudWatch Logs 확인
-> 리소스 삭제
```

## 주요 AWS 서비스

| 서비스 | 역할 |
| --- | --- |
| IAM | 사용자, 권한, Access Key 관리 |
| Billing/Budgets | 비용 확인과 예산 알림 |
| ECR | Docker image 저장소 |
| App Runner | 컨테이너 image를 웹 서비스로 배포 |
| CloudWatch Logs | App Runner 실행 로그 확인 |

## App Runner를 기본으로 사용하는 이유

초보자에게 ECS, VPC, Load Balancer, Task Definition까지 한 번에 다루는 것은 부담이 큽니다. 07 과정에서는 먼저 App Runner로 ECR image를 배포하고 `/health`와 CloudWatch Logs를 확인합니다.

ECS는 운영 심화 주제로 설명하거나 팀 프로젝트 확장으로 다룹니다.

## 필수 확인 명령

```powershell
aws --version
aws sts get-caller-identity
aws configure get region
aws ecr describe-repositories --region ap-northeast-2
```

ECR push 후:

```powershell
aws ecr describe-images `
  --repository-name aidev-auto-healing-agent `
  --region ap-northeast-2
```

CloudWatch:

```powershell
aws logs describe-log-groups --region ap-northeast-2
```

## 보안 기준

- AWS Access Key를 코드, README, 발표 자료, GitHub Actions 로그에 노출하지 않습니다.
- `.env`는 커밋하지 않습니다.
- GitHub Actions에서 AWS에 접근할 때는 repository secret 또는 OIDC를 사용합니다.
- 운영 환경에서는 장기 Access Key보다 OIDC 기반 인증을 권장합니다.

## 비용 기준

- 배포 전 Budget을 설정합니다.
- App Runner, ECR, CloudWatch Logs는 실습 후 삭제합니다.
- 삭제 후 Billing Dashboard에서 비용을 확인합니다.
