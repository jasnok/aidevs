# SETUP

이 문서는 `07_multi-agent-service-ops`의 로컬 실행, GitHub Actions, AWS 배포, CloudWatch 확인, 리소스 삭제까지 안내하는 설정 문서입니다.

07 과정에서는 AWS 배포가 필수 실습입니다. 비용이 발생할 수 있으므로 **예산 알림 설정, 실습 후 리소스 삭제, 비용 확인**까지 실습 범위에 포함합니다.

## 0. 공통 준비 문서

아래 항목이 아직 준비되지 않았다면 먼저 공통 설치 가이드를 확인합니다.

| 필요한 내용 | 문서 |
| --- | --- |
| Python과 `.venv` | [`../00_course-guide/02_setup-guides/01_python-install-guide.md`](../00_course-guide/02_setup-guides/01_python-install-guide.md), [`../00_course-guide/02_setup-guides/06_venv-pip-requirements-guide.md`](../00_course-guide/02_setup-guides/06_venv-pip-requirements-guide.md) |
| Git/GitHub | [`../00_course-guide/02_setup-guides/04_git-github-setup-guide.md`](../00_course-guide/02_setup-guides/04_git-github-setup-guide.md) |
| Docker Desktop | [`../00_course-guide/02_setup-guides/14_docker-desktop-guide.md`](../00_course-guide/02_setup-guides/14_docker-desktop-guide.md) |
| AWS 계정과 비용 관리 | [`../00_course-guide/02_setup-guides/15_aws-account-and-cost-guide.md`](../00_course-guide/02_setup-guides/15_aws-account-and-cost-guide.md) |
| GitHub Actions | [`../00_course-guide/02_setup-guides/16_github-actions-guide.md`](../00_course-guide/02_setup-guides/16_github-actions-guide.md) |
| Codex와 ChatGPT 사용 준비 | [`../00_course-guide/02_setup-guides/17_codex-chatgpt-guide.md`](../00_course-guide/02_setup-guides/17_codex-chatgpt-guide.md) |
| 문제 해결 | [`../00_course-guide/03_learning-support/troubleshooting.md`](../00_course-guide/03_learning-support/troubleshooting.md) |

## 1. 사용하는 도구

| 도구 | 사용 이유 |
| --- | --- |
| Python `.venv` | 로컬 예제와 Agent 코드를 실행합니다. |
| FastAPI | backend API와 `/health` endpoint를 만듭니다. |
| Streamlit | frontend와 monitor 화면을 만듭니다. |
| Dockerfile | Python 서비스를 Docker image로 패키징합니다. |
| Docker Compose | backend, frontend, worker, monitor를 함께 실행합니다. |
| Git/GitHub | 코드 변경과 GitHub Actions 실행을 관리합니다. |
| GitHub Actions | Python 문법 검사, Compose config 검증, Docker build를 자동 실행합니다. |
| AWS ECR | Docker image를 저장합니다. |
| AWS App Runner | ECR image를 서비스로 배포합니다. |
| CloudWatch Logs | 배포된 서비스의 실행 로그를 확인합니다. |

## 2. 작업 폴더와 가상환경

```powershell
cd C:\aidev\07_multi-agent-service-ops
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

현재 Python이 07 과정 `.venv`를 사용하는지 확인합니다.

```powershell
python -c "import sys; print(sys.executable)"
```

정상 예시:

```text
C:\aidev\07_multi-agent-service-ops\.venv\Scripts\python.exe
```

## 3. `.env`와 비밀값 관리

```powershell
Copy-Item .env.example .env
```

`.env`에는 실제 값을 작성합니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4o-mini
AWS_REGION=ap-northeast-2
AWS_ACCOUNT_ID=123456789012
ECR_REPOSITORY_NAME=aidev-auto-healing-agent
APP_RUNNER_SERVICE_NAME=aidev-auto-healing-agent
```

주의:

- `.env`는 GitHub에 올리지 않습니다.
- OpenAI API Key, AWS Access Key, 비밀번호는 코드와 README에 적지 않습니다.
- GitHub Actions에 필요한 값은 GitHub Repository의 `Settings > Secrets and variables > Actions`에 저장합니다.

## 4. Docker Desktop 확인

Docker Desktop을 실행한 뒤 확인합니다.

```powershell
docker --version
docker compose version
docker ps
docker run hello-world
```

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 먼저 확인합니다.

## 5. Docker Compose 기본 확인

Docker Compose는 여러 컨테이너를 하나의 `docker-compose.yml`로 함께 실행하는 도구입니다.

07 과정의 기본 서비스 구성:

```text
backend  : FastAPI API 서버
frontend : Streamlit 사용자 화면
worker   : 장애 메시지 처리와 복구 action 결정
monitor  : 서비스 상태와 운영 로그 표시
```

자주 쓰는 명령:

```powershell
docker compose config
docker compose up --build
docker compose up --build -d
docker compose ps
docker compose logs backend
docker compose logs -f worker
docker compose down
```

## 6. 단일 FastAPI Docker 서비스 실행

먼저 작은 FastAPI 서비스를 Docker image로 만들고 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

실행 중인 PowerShell에서 `Ctrl + C`를 눌러 종료합니다.

## 7. Docker Compose 멀티 서비스 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

확인 명령:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

종료:

```powershell
docker compose down
```

## 8. Git과 GitHub 준비

```powershell
git --version
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

기본 흐름:

```powershell
cd C:\aidev
git status
git add 07_multi-agent-service-ops
git commit -m "docs: update service ops course"
git push
```

## 9. GitHub Actions 준비

예제 workflow 위치:

```text
C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\04_github-actions-cicd\.github\workflows\docker-build-check.yml
```

GitHub에서 자동 실행하려면 repository 기준 `.github/workflows` 아래에 workflow 파일이 있어야 합니다.

전체 `C:\aidev`를 하나의 GitHub repository로 사용한다면 다음 위치에 복사합니다.

```text
C:\aidev\.github\workflows\docker-build-check.yml
```

처음에는 배포 자동화보다 다음 자동 검증에 집중합니다.

```text
push 또는 pull request
-> Python 문법 검사
-> Docker Compose config 검증
-> Docker image build 검증
-> GitHub Actions 로그 확인
```

## 10. AWS 계정 준비

AWS 실습은 필수입니다. 비용과 보안 사고를 줄이기 위해 아래 항목을 먼저 확인합니다.

1. AWS 계정에 로그인합니다.
2. 루트 계정 사용은 피하고 IAM 사용자 또는 IAM Identity Center 사용을 권장합니다.
3. 루트 계정과 관리자 계정에 MFA를 활성화합니다.
4. 수업에서 사용할 리전을 정합니다. 예: `ap-northeast-2`
5. Billing Dashboard 접근 가능 여부를 확인합니다.

AWS Console에서 자주 사용할 서비스:

| 서비스 | 역할 |
| --- | --- |
| IAM | 사용자, 권한, Access Key 관리 |
| Billing | 비용 확인 |
| Budgets | 비용 알림 설정 |
| ECR | Docker image 저장 |
| App Runner | 컨테이너 서비스 배포 |
| CloudWatch | 로그와 지표 확인 |

## 11. AWS 비용 안전장치

AWS 배포 전 다음을 설정합니다.

1. AWS Console에서 `Billing and Cost Management`로 이동합니다.
2. `Budgets`를 엽니다.
3. 실습용 월 예산을 만듭니다. 예: 10~30 USD
4. 이메일 알림을 설정합니다.
5. 실습 후 삭제할 리소스 목록을 미리 확인합니다.

실습 후 삭제 대상:

- App Runner service
- ECR image
- ECR repository
- CloudWatch Log Group
- 사용하지 않는 IAM Access Key
- 불필요한 GitHub Actions secrets

## 12. AWS CLI 설치와 인증 확인

AWS CLI 설치 후 확인합니다.

```powershell
aws --version
```

Access Key 기반으로 설정할 경우:

```powershell
aws configure
```

입력 항목:

```text
AWS Access Key ID
AWS Secret Access Key
Default region name: ap-northeast-2
Default output format: json
```

인증 확인:

```powershell
aws sts get-caller-identity
aws configure get region
```

주의:

- Access Key는 GitHub에 올리지 않습니다.
- 실습 후 필요하지 않은 Access Key는 비활성화하거나 삭제합니다.
- 운영 환경에서는 장기 Access Key보다 IAM Role 또는 GitHub OIDC 사용을 권장합니다.

## 13. ECR repository 준비

변수 예시:

```powershell
$env:AWS_REGION="ap-northeast-2"
$env:AWS_ACCOUNT_ID="123456789012"
$env:ECR_REPOSITORY_NAME="aidev-auto-healing-agent"
```

ECR repository 생성:

```powershell
aws ecr create-repository `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

이미 존재한다는 오류가 나오면 같은 repository를 계속 사용하면 됩니다.

ECR 로그인:

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
docker login --username AWS --password-stdin "$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"
```

## 14. Docker image tag와 push

단일 FastAPI 예제를 AWS에 올립니다.

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
```

ECR 주소:

```powershell
$env:ECR_IMAGE_URI="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com/$env:ECR_REPOSITORY_NAME:latest"
```

tag와 push:

```powershell
docker tag aidev-agent-backend:local $env:ECR_IMAGE_URI
docker push $env:ECR_IMAGE_URI
```

ECR에서 image 확인:

```powershell
aws ecr describe-images `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

## 15. App Runner 배포

초보자 기준으로 07 과정의 기본 AWS 배포 대상은 App Runner입니다.

AWS Console 흐름:

1. AWS Console에서 `App Runner`를 엽니다.
2. `Create service`를 선택합니다.
3. Source로 `Container registry`를 선택합니다.
4. Provider는 `Amazon ECR`을 선택합니다.
5. 방금 push한 ECR image를 선택합니다.
6. Deployment trigger는 수업 상황에 맞게 manual 또는 automatic을 선택합니다.
7. Service name을 입력합니다. 예: `aidev-auto-healing-agent`
8. Port는 FastAPI 컨테이너가 사용하는 `8000`으로 설정합니다.
9. 필요한 환경 변수를 추가합니다.
10. Service 생성 후 배포가 완료될 때까지 기다립니다.

배포 완료 후 App Runner URL을 확인합니다.

```text
https://xxxxx.ap-northeast-2.awsapprunner.com/health
```

브라우저 또는 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod https://your-apprunner-url/health
```

## 16. CloudWatch Logs 확인

App Runner 배포 후 로그를 확인합니다.

AWS Console 흐름:

1. `CloudWatch`를 엽니다.
2. `Logs > Log groups`로 이동합니다.
3. App Runner service 이름과 관련된 Log Group을 찾습니다.
4. 배포 로그와 애플리케이션 로그를 확인합니다.
5. `/health` 요청이 기록되는지 확인합니다.

CLI로 확인할 때:

```powershell
aws logs describe-log-groups --region $env:AWS_REGION
```

Log Group 이름을 확인한 뒤:

```powershell
aws logs describe-log-streams `
  --log-group-name "your-log-group-name" `
  --region $env:AWS_REGION
```

## 17. GitHub Actions와 AWS 연결

기본 수업에서는 GitHub Actions로 Python 문법 검사, Compose config 검증, Docker build 검증을 먼저 합니다.

AWS push/deploy까지 자동화하려면 GitHub repository secret이 필요합니다.

필요한 secret 예시:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ACCOUNT_ID
ECR_REPOSITORY_NAME
```

주의:

- GitHub Actions 로그에 secret이 출력되지 않도록 합니다.
- 운영 환경에서는 OIDC 기반 인증을 권장합니다.
- 자동 배포 전에 수동 ECR push와 App Runner 배포가 성공하는지 먼저 확인합니다.

## 18. 실습 후 AWS 리소스 삭제

실습 종료 후 반드시 삭제합니다.

App Runner service 삭제:

1. App Runner Console로 이동합니다.
2. 실습 service를 선택합니다.
3. `Actions > Delete`를 실행합니다.
4. 삭제 완료 상태를 확인합니다.

ECR image/repository 삭제:

```powershell
aws ecr list-images `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

repository 전체 삭제:

```powershell
aws ecr delete-repository `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --force `
  --region $env:AWS_REGION
```

CloudWatch Log Group 삭제:

1. CloudWatch Console로 이동합니다.
2. 실습에서 생성된 Log Group을 찾습니다.
3. 필요 없는 Log Group을 삭제합니다.

Access Key 정리:

1. IAM Console로 이동합니다.
2. 실습용 사용자 또는 Access Key를 확인합니다.
3. 더 이상 사용하지 않는 Access Key를 비활성화하거나 삭제합니다.

비용 확인:

1. Billing Dashboard에서 현재 비용을 확인합니다.
2. Budgets 알림이 정상 설정되어 있는지 확인합니다.

## 19. 전체 점검 체크리스트

- [ ] 07 과정 `.venv`가 활성화되어 있다.
- [ ] Docker Desktop이 실행 중이다.
- [ ] `docker compose config`가 성공한다.
- [ ] 단일 FastAPI Docker image가 build/run 된다.
- [ ] Docker Compose로 backend/frontend/worker/monitor가 실행된다.
- [ ] GitHub Actions가 Python 문법 검사와 Docker build를 수행한다.
- [ ] ECR repository를 생성했다.
- [ ] Docker image를 ECR에 push했다.
- [ ] App Runner에 서비스를 배포했다.
- [ ] 배포 URL `/health`가 응답한다.
- [ ] CloudWatch Logs에서 실행 로그를 확인했다.
- [ ] App Runner, ECR, CloudWatch 리소스를 삭제했다.
- [ ] Billing Dashboard에서 비용을 확인했다.

## 20. 자주 막히는 오류

| 증상 | 확인할 것 |
| --- | --- |
| `docker` 명령을 찾을 수 없음 | Docker Desktop 설치와 재시작 여부 |
| `docker ps` 실패 | Docker Desktop 실행 여부 |
| `docker compose config` 실패 | `docker-compose.yml` 들여쓰기, `.env` 존재 여부 |
| port already allocated | 기존 컨테이너 또는 서버가 같은 포트를 사용 중인지 확인 |
| ECR login 실패 | AWS CLI 인증, 리전, 계정 ID 확인 |
| `docker push` 권한 오류 | ECR repository 이름, IAM 권한 확인 |
| App Runner health check 실패 | 컨테이너 port, `/health`, startup command 확인 |
| CloudWatch 로그가 없음 | App Runner 배포 상태와 Log Group 이름 확인 |
| AWS 비용 걱정 | 실습 후 리소스 삭제, Billing Dashboard 확인 |
