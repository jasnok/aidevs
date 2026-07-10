# 06 AWS Cleanup And Cost Control

AWS 배포 실습 후에는 리소스를 삭제하고 비용을 확인합니다. 이 단계까지 완료해야 AWS 배포 실습이 끝난 것으로 봅니다.

## 삭제 대상

| 리소스 | 삭제 이유 |
| --- | --- |
| App Runner service | 실행 중이면 비용이 발생할 수 있습니다. |
| ECR image/repository | 저장소와 image를 정리합니다. |
| CloudWatch Log Group | 로그 저장 비용을 줄입니다. |
| IAM Access Key | 실습 후 사용하지 않는 key를 제거합니다. |
| GitHub Actions secrets | 더 이상 필요 없는 secret을 삭제합니다. |

## 1. App Runner service 삭제

AWS Console:

1. App Runner로 이동합니다.
2. 실습 service를 선택합니다.
3. `Actions > Delete`를 선택합니다.
4. 삭제 완료 상태를 확인합니다.

## 2. ECR repository 삭제

PowerShell:

```powershell
$env:AWS_REGION="ap-northeast-2"
$env:ECR_REPOSITORY_NAME="aidev-auto-healing-agent"
```

image 확인:

```powershell
aws ecr list-images `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --region $env:AWS_REGION
```

repository 삭제:

```powershell
aws ecr delete-repository `
  --repository-name $env:ECR_REPOSITORY_NAME `
  --force `
  --region $env:AWS_REGION
```

## 3. CloudWatch Log Group 삭제

Log Group 목록 확인:

```powershell
aws logs describe-log-groups --region $env:AWS_REGION
```

삭제할 Log Group 이름을 확인한 뒤 AWS Console에서 삭제하거나 CLI를 사용합니다.

```powershell
aws logs delete-log-group `
  --log-group-name "your-log-group-name" `
  --region $env:AWS_REGION
```

## 4. Access Key 정리

1. IAM Console로 이동합니다.
2. 실습용 사용자를 선택합니다.
3. `Security credentials`에서 Access Key를 확인합니다.
4. 더 이상 사용하지 않으면 비활성화하거나 삭제합니다.

## 5. 비용 확인

1. Billing Dashboard를 엽니다.
2. 현재 비용과 Forecast를 확인합니다.
3. Budgets 알림이 정상 설정되어 있는지 확인합니다.

## 제출 체크리스트

- [ ] App Runner service 삭제 완료
- [ ] ECR repository 삭제 완료
- [ ] CloudWatch Log Group 삭제 완료
- [ ] 불필요한 Access Key 정리 완료
- [ ] Billing Dashboard 비용 확인 완료
- [ ] 삭제 확인 내용을 최종 프로젝트 산출물에 기록
