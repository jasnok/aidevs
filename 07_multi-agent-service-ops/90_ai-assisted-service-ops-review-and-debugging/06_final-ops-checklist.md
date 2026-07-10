# 06 Final Ops Checklist

최종 제출 전 운영 관점에서 확인합니다.

## 로컬 실행

- [ ] `.venv`가 정상이다.
- [ ] Docker Desktop이 실행 중이다.
- [ ] `docker compose config`가 성공한다.
- [ ] `docker compose up --build`가 성공한다.
- [ ] backend `/health`가 응답한다.
- [ ] frontend와 monitor가 열린다.

## 자동 검증

- [ ] GitHub Actions workflow가 존재한다.
- [ ] Python 문법 검사 step이 성공한다.
- [ ] Docker Compose config step이 성공한다.
- [ ] Docker build step이 성공한다.

## AWS

- [ ] ECR repository를 생성했다.
- [ ] Docker image를 ECR에 push했다.
- [ ] App Runner 배포가 성공했다.
- [ ] 배포 URL `/health`가 응답한다.
- [ ] CloudWatch Logs를 확인했다.

## 보안과 운영

- [ ] `.env`가 커밋되지 않았다.
- [ ] API Key와 Access Key가 로그에 노출되지 않았다.
- [ ] Prompt Injection 방어 기준이 있다.
- [ ] Tool 권한 정책이 있다.
- [ ] Auto Healing 복구 결과가 기록된다.

## 정리

- [ ] App Runner service를 삭제했다.
- [ ] ECR repository를 삭제했다.
- [ ] CloudWatch Log Group을 삭제했다.
- [ ] Billing Dashboard에서 비용을 확인했다.
