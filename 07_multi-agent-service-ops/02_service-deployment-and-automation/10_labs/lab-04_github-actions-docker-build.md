# Lab 04. GitHub Actions Docker Build

## 목표

GitHub Actions로 Docker build 검증을 자동화하는 흐름을 이해합니다.

## 확인할 파일

```text
02_service-deployment-and-automation/04_github-actions-cicd/.github/workflows/docker-build-check.yml
```

## 작성할 내용

- workflow가 실행되는 조건
- Docker build 대상 경로
- 실패했을 때 확인할 로그
- API Key를 workflow에 직접 쓰면 안 되는 이유

## 확장 과제

저장소 루트의 `.github/workflows` 위치로 workflow를 옮기면 GitHub에서 자동 실행할 수 있습니다.
