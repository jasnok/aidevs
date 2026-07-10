# 05 AWS Deployment Basic

이 실습은 `01_docker-service-packaging`의 작은 FastAPI 서비스를 AWS에 배포하는 기본 흐름입니다.

07 과정에서 AWS 배포는 필수 실습입니다. 비용이 발생할 수 있으므로 배포 전 Budget을 설정하고, 실습 후 리소스를 삭제합니다.

## 배포 대상

```text
02_service-deployment-and-automation/01_docker-service-packaging
```

이 폴더에는 다음 파일이 있습니다.

```text
app/main.py
requirements.txt
Dockerfile
```

서비스는 `/health` endpoint를 제공합니다.

## 1. 로컬 Docker build

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
```

## 2. 로컬 실행 확인

PowerShell 1:

```powershell
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

PowerShell 2:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## 3. AWS 변수 준비

```powershell
$env:AWS_REGION="ap-northeast-2"
$env:AWS_ACCOUNT_ID="123456789012"
$env:ECR_REPOSITORY_NAME="aidev-auto-healing-agent"
```

본인의 AWS 계정 ID로 `AWS_ACCOUNT_ID`를 바꿉니다.

확인:

```powershell
aws sts get-caller-identity
aws configure get region
```

## 4. ECR repository 생성

```powershell
aws ecr create-repository `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

이미 존재한다는 메시지가 나오면 다음 단계로 넘어갑니다.

## 5. ECR login

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
docker login --username AWS --password-stdin "$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"
```

## 6. image tag/push

```powershell
$env:ECR_IMAGE_URI="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com/$env:ECR_REPOSITORY_NAME:latest"
docker tag aidev-agent-backend:local $env:ECR_IMAGE_URI
docker push $env:ECR_IMAGE_URI
```

확인:

```powershell
aws ecr describe-images `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

## 7. App Runner 배포

AWS Console에서 진행합니다.

1. App Runner를 엽니다.
2. `Create service`를 선택합니다.
3. Source는 `Container registry`를 선택합니다.
4. Provider는 `Amazon ECR`을 선택합니다.
5. 방금 push한 image를 선택합니다.
6. Service name을 입력합니다. 예: `aidev-auto-healing-agent`
7. Port는 `8000`으로 설정합니다.
8. 환경 변수가 필요한 경우 추가합니다.
9. Service 생성을 완료합니다.

## 8. 배포 URL 확인

배포가 끝나면 App Runner URL이 생성됩니다.

```text
https://xxxxx.ap-northeast-2.awsapprunner.com
```

확인:

```powershell
Invoke-RestMethod https://your-apprunner-url/health
```

## 9. CloudWatch Logs 확인

1. CloudWatch를 엽니다.
2. `Logs > Log groups`로 이동합니다.
3. App Runner service와 관련된 Log Group을 찾습니다.
4. 배포 로그와 `/health` 요청 로그를 확인합니다.

CLI:

```powershell
aws logs describe-log-groups --region $env:AWS_REGION
```

## 10. 다음 단계

배포 확인 후 반드시 다음 문서로 이동합니다.

```text
../06_aws-cleanup-and-cost-control/README.md
```

실습이 끝났다면 App Runner, ECR, CloudWatch 리소스를 삭제합니다.
