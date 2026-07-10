# Assignment 01. Auto Healing Workflow Design

## 과제 목표

팀 미니 프로젝트에 적용할 Auto Healing 워크플로우를 설계합니다.

## 필수 작성 내용

1. 대상 서비스 목록
2. 서비스별 Health Check URL 또는 점검 방법
3. 장애 유형 4개 이상
4. 장애 유형별 복구 조치
5. Retry/Restart/Escalate 기준
6. 복구 결과 검증 기준
7. 운영 로그에 남길 이벤트 목록
8. Docker Compose 또는 AWS에서 확장할 방법

## 제출 형식

Markdown 문서로 제출합니다.

```text
team-name_auto-healing-workflow-design.md
```

## 평가 기준

- 장애 유형과 복구 조치가 논리적으로 연결되는가?
- 무조건 재시작하지 않고 단계적 대응을 설계했는가?
- 복구 후 검증 기준이 있는가?
- Docker/AWS 운영 관점이 반영되어 있는가?
