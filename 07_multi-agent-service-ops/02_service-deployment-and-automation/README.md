# 02_service-deployment-and-automation

이 단원은 작은 FastAPI 서비스를 Docker, Docker Compose, GitHub Actions, AWS 배포까지 전개하는 실습 단원입니다.

실습 기준 프로젝트는 `01_docker-service-packaging`의 FastAPI `/health` 예제입니다. 이 예제를 Docker image로 만들고, Compose로 여러 서비스 실행 구조를 확인한 뒤, GitHub Actions 자동 검증과 AWS ECR/App Runner 배포까지 연결합니다.

## 단원 구조

```text
02_service-deployment-and-automation
├─ 01_docker-service-packaging
├─ 02_docker-compose-multi-service
├─ 03_service-health-and-runtime
├─ 04_github-actions-cicd
├─ 05_aws-deployment-basic
├─ 06_aws-cleanup-and-cost-control
├─ 10_labs
└─ 20_assignments
```

## 실습 흐름

```text
FastAPI /health 예제 확인
-> Dockerfile로 image build
-> docker run으로 local container 실행
-> Docker Compose로 backend/frontend/worker/monitor 실행
-> GitHub Actions에서 Python/Compose/Docker build 검증
-> ECR repository 생성
-> image tag/push
-> App Runner 배포
-> 배포 URL /health 확인
-> CloudWatch Logs 확인
-> AWS 리소스 삭제와 비용 확인
```

## 필수 확인

- [ ] Docker image build 성공
- [ ] local container `/health` 응답
- [ ] Docker Compose config 성공
- [ ] Docker Compose 서비스 실행
- [ ] GitHub Actions build 검증 성공
- [ ] ECR image push 성공
- [ ] App Runner 배포 성공
- [ ] CloudWatch Logs 확인
- [ ] AWS 리소스 삭제
