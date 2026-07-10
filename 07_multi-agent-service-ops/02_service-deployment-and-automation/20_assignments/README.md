# 20 Assignments

## 과제. Docker Compose와 AWS 배포 운영 보고서

작은 FastAPI 서비스를 Docker로 패키징하고, Docker Compose로 로컬 운영 구조를 확인한 뒤, GitHub Actions와 AWS 배포 결과를 운영 관점에서 정리합니다.

## 제출 내용

- 서비스 구성도
- `docker build` 결과
- `docker run` 후 `/health` 확인 결과
- `docker compose config` 결과 요약
- `docker compose ps` 결과
- backend/worker/monitor 로그 확인 결과
- GitHub Actions 실행 결과
- ECR image push 결과
- App Runner 배포 URL과 `/health` 확인 결과
- CloudWatch Logs 확인 결과
- AWS 리소스 삭제 결과
- 비용 확인 결과

## 평가 기준

- Docker image와 Compose 구조를 설명할 수 있는가?
- GitHub Actions 자동 검증 흐름을 이해했는가?
- AWS ECR/App Runner 배포를 완료했는가?
- CloudWatch Logs에서 실행 로그를 확인했는가?
- 실습 후 AWS 리소스를 삭제했는가?
- 운영 관점에서 health check, logs, 비용, 보안을 함께 설명했는가?
