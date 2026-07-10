# 05 CloudWatch Log Review

이 폴더는 AWS App Runner로 배포한 서비스의 CloudWatch Logs를 확인하는 실습 문서입니다.

## 목표

- App Runner 배포 로그를 찾습니다.
- 애플리케이션 실행 로그를 확인합니다.
- `/health` 요청 로그를 확인합니다.
- 장애 상황과 Auto Healing 이벤트를 어떤 로그로 남겨야 하는지 정리합니다.

## Console 확인 흐름

1. AWS Console에서 CloudWatch를 엽니다.
2. `Logs > Log groups`로 이동합니다.
3. App Runner service 이름과 관련된 Log Group을 찾습니다.
4. 최신 Log Stream을 엽니다.
5. 배포 로그, startup 로그, `/health` 요청 로그를 확인합니다.

## CLI 확인 명령

리전 설정:

```powershell
$env:AWS_REGION="ap-northeast-2"
```

Log Group 목록:

```powershell
aws logs describe-log-groups --region $env:AWS_REGION
```

Log Stream 목록:

```powershell
aws logs describe-log-streams `
  --log-group-name "your-log-group-name" `
  --region $env:AWS_REGION
```

## 기록할 내용

| 항목 | 값 |
| --- | --- |
| App Runner service |  |
| App Runner URL |  |
| CloudWatch Log Group |  |
| 확인한 Log Stream |  |
| `/health` 요청 로그 확인 여부 |  |
| 오류 로그 여부 |  |

## 운영 관점 질문

- 장애가 발생했을 때 어떤 로그로 원인을 찾을 수 있는가?
- Auto Healing action이 실행되었다면 어떤 event 이름으로 남길 것인가?
- 정책 위반이나 권한 오류는 어떤 로그 필드로 남길 것인가?
- 로그에 API Key나 개인정보가 노출되지 않는가?
