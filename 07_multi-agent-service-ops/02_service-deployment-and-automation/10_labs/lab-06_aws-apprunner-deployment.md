# Lab 06. AWS App Runner Deployment

이 lab은 작은 FastAPI Docker image를 AWS ECR에 push하고 App Runner로 배포하는 실습입니다.

## 목표

- ECR repository를 생성합니다.
- Docker image를 tag/push합니다.
- App Runner service를 생성합니다.
- 배포 URL의 `/health`를 확인합니다.
- CloudWatch Logs를 확인합니다.

## 실습 대상

```text
02_service-deployment-and-automation/01_docker-service-packaging
```

## 완료 기록

| 항목 | 값 |
| --- | --- |
| AWS Region |  |
| ECR Repository |  |
| ECR Image URI |  |
| App Runner URL |  |
| CloudWatch Log Group |  |

## 완료 기준

- [ ] ECR image push 성공
- [ ] App Runner 배포 성공
- [ ] `/health` 응답 확인
- [ ] CloudWatch Logs 확인
- [ ] 다음 lab에서 리소스 삭제 진행
