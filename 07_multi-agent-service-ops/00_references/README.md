# 00_references

이 폴더는 `07_multi-agent-service-ops`의 참고 문서 모음입니다.

07 과정은 멀티 에이전트 협업 구조를 서비스 운영 흐름으로 확장합니다. Docker Compose로 로컬 서비스를 실행하고, GitHub Actions로 자동 검증을 수행하며, AWS ECR/App Runner에 배포하고 CloudWatch Logs에서 실행 로그를 확인합니다.

## 문서 목록

| 파일 | 내용 |
| --- | --- |
| `01_course-big-picture.md` | 07 과정 전체 흐름과 05~06 과정과의 연결 |
| `02_environment-checklist.md` | Python, Docker, GitHub, AWS 환경 점검 |
| `03_multi-agent-service-map.md` | Multi-Agent 서비스 구성과 역할 |
| `04_docker-compose-and-service-ops.md` | Docker Compose 기반 운영 구조 |
| `05_aws-deployment-map.md` | ECR, App Runner, CloudWatch 배포 흐름 |
| `06_security-guardrails-overview.md` | Prompt Injection, 권한, 정책 검증 |
| `07_auto-healing-overview.md` | 장애 감지와 자동 복구 흐름 |
| `08_observability-ops-dashboard.md` | 로그, trace, 운영 대시보드 |
| `09_common-errors-for-beginners.md` | 자주 막히는 오류와 확인 명령 |
| `10_final-project-roadmap.md` | 최종 Auto Healing 프로젝트 진행 로드맵 |
| `11_course-alignment-checklist.md` | 커리큘럼 요구사항과 현재 폴더 매핑 |
| `12_aws-cost-and-cleanup-checklist.md` | AWS 비용 안전장치와 리소스 삭제 체크리스트 |

## 07 과정에서 반드시 확인할 것

- Docker Compose로 서비스가 로컬에서 실행되는가?
- GitHub Actions에서 Docker build 검증이 성공하는가?
- ECR에 image를 push하고 App Runner로 배포할 수 있는가?
- CloudWatch Logs에서 배포된 서비스 로그를 확인할 수 있는가?
- 장애 감지, retry, restart, fallback 흐름을 설명할 수 있는가?
- Prompt Injection, Tool 권한, Agent 접근 제어 기준을 설명할 수 있는가?
- 실습 후 AWS 리소스를 삭제하고 비용을 확인했는가?
