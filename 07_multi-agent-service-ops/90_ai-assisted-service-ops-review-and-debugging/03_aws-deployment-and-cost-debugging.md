# 03 AWS Deployment And Cost Debugging

## 확인 명령

```powershell
aws --version
aws sts get-caller-identity
aws configure get region
aws ecr describe-repositories --region ap-northeast-2
aws logs describe-log-groups --region ap-northeast-2
```

## 자주 보는 문제

| 증상 | 확인할 것 |
| --- | --- |
| ECR login 실패 | AWS 인증, region, account id |
| docker push 실패 | ECR repository 이름, IAM 권한 |
| App Runner 배포 실패 | image URI, port 8000, health check |
| `/health`가 응답 없음 | FastAPI 실행 명령, App Runner port |
| CloudWatch 로그를 못 찾음 | App Runner service 이름, Log Group |
| 비용이 계속 발생 | App Runner service, ECR, CloudWatch 삭제 여부 |

## Codex 질문 예시

```text
App Runner 배포가 실패했습니다.
배포 대상: ECR image
컨테이너 포트: 8000
health endpoint: /health
App Runner 이벤트 로그:
...
CloudWatch 로그:
...
어떤 설정을 먼저 확인해야 하나요?
```

## 비용 점검

- Billing Dashboard 확인
- Budgets 알림 확인
- App Runner service 삭제
- ECR repository 삭제
- CloudWatch Log Group 삭제
