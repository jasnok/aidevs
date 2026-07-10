# 10 Final Project Roadmap

최종 프로젝트는 `99_final-service-ops-project`에서 진행합니다.

주제:

```text
에러 자가 치유(Auto Healing) 워크플로우
```

## 권장 진행 순서

```text
1. sample-auto-healing-agent 로컬 실행
2. Docker Compose로 backend/frontend/worker/monitor 실행
3. Multi-Agent 역할과 협업 흐름 정리
4. 장애 유형과 복구 전략 정의
5. retry/restart/fallback 정책 구현
6. 보안/가드레일 정책 적용
7. 운영 로그와 monitor 화면 확인
8. GitHub Actions 자동 검증 실행
9. ECR image push
10. App Runner 배포
11. 배포 URL /health 확인
12. CloudWatch Logs 확인
13. Auto Healing 결과 보고서 작성
14. AWS 리소스 삭제
15. 최종 발표 문서 정리
```

## 필수 산출물

- Multi-Agent 협업 구조 설계서
- Docker Compose 실행 결과
- GitHub Actions 실행 결과
- AWS 배포 결과 보고서
- CloudWatch Logs 확인 결과
- Auto Healing 장애 대응 결과 보고서
- 보안/가드레일 정책 문서
- AWS 리소스 삭제 체크리스트

## 최종 프로젝트 완료 기준

- 로컬에서 `docker compose up --build`로 서비스가 실행됩니다.
- backend `/health`가 정상 응답합니다.
- GitHub Actions에서 Docker build 검증이 성공합니다.
- AWS App Runner 배포 URL에서 `/health`가 정상 응답합니다.
- CloudWatch Logs에서 배포 서비스 로그를 확인합니다.
- 장애 메시지에 대해 복구 action이 선택되고 결과가 기록됩니다.
- Prompt Injection 또는 Tool 권한 위반을 차단하는 기준이 있습니다.
- 실습 후 AWS 리소스를 삭제하고 비용을 확인합니다.
