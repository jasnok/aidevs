# Lab 06. CloudWatch Log Review

AWS App Runner 배포 후 CloudWatch Logs에서 서비스 실행 로그를 확인합니다.

## 목표

- App Runner service와 연결된 Log Group을 찾습니다.
- 배포 로그와 애플리케이션 로그를 확인합니다.
- `/health` 요청 로그를 확인합니다.
- 오류 로그가 있다면 원인을 정리합니다.

## 진행 순서

1. AWS Console에서 CloudWatch를 엽니다.
2. `Logs > Log groups`로 이동합니다.
3. App Runner service 이름과 관련된 Log Group을 찾습니다.
4. 최신 Log Stream을 엽니다.
5. `/health` 요청 전후의 로그를 확인합니다.

## CLI 확인

```powershell
$env:AWS_REGION="ap-northeast-2"
aws logs describe-log-groups --region $env:AWS_REGION
```

## 기록

| 항목 | 값 |
| --- | --- |
| App Runner service |  |
| App Runner URL |  |
| Log Group |  |
| Log Stream |  |
| 확인한 정상 로그 |  |
| 확인한 오류 로그 |  |

## 완료 기준

- [ ] CloudWatch Log Group을 찾았다.
- [ ] Log Stream을 열었다.
- [ ] `/health` 요청 로그를 확인했다.
- [ ] 로그에 비밀값이 노출되지 않는지 확인했다.
