# 12 AWS Cost And Cleanup Checklist

AWS 실습은 07 과정의 필수 실습입니다. 실습 전 비용 안전장치를 설정하고, 실습 후 리소스를 삭제합니다.

## 실습 전

- [ ] AWS 계정에 로그인했다.
- [ ] 루트 계정 대신 IAM 사용자 또는 IAM Identity Center를 사용한다.
- [ ] MFA를 활성화했다.
- [ ] 실습 리전을 정했다. 예: `ap-northeast-2`
- [ ] Billing Dashboard를 열 수 있다.
- [ ] AWS Budget 또는 비용 알림을 만들었다.
- [ ] AWS CLI가 설치되어 있다.
- [ ] `aws sts get-caller-identity`가 성공한다.
- [ ] `aws configure get region` 결과가 실습 리전과 일치한다.

## 배포 중

- [ ] ECR repository 이름을 기록했다.
- [ ] ECR image URI를 기록했다.
- [ ] App Runner service 이름을 기록했다.
- [ ] App Runner 배포 URL을 기록했다.
- [ ] CloudWatch Log Group 이름을 기록했다.
- [ ] GitHub Actions에 등록한 secret 목록을 기록했다.

## 실습 후 삭제

- [ ] App Runner service를 삭제했다.
- [ ] ECR image를 삭제했다.
- [ ] ECR repository를 삭제했다.
- [ ] CloudWatch Log Group을 삭제했다.
- [ ] 실습용 IAM Access Key를 비활성화하거나 삭제했다.
- [ ] 불필요한 GitHub Actions secret을 삭제했다.
- [ ] Billing Dashboard에서 비용을 확인했다.

## 기록 양식

| 항목 | 값 |
| --- | --- |
| AWS Region |  |
| ECR Repository |  |
| ECR Image URI |  |
| App Runner Service |  |
| App Runner URL |  |
| CloudWatch Log Group |  |
| 삭제 확인 일시 |  |

## 주의

- App Runner service가 남아 있으면 비용이 계속 발생할 수 있습니다.
- CloudWatch Logs도 저장량에 따라 비용이 발생할 수 있습니다.
- Access Key는 실습 후 사용하지 않으면 삭제하는 것이 안전합니다.
