# 04 GitHub Actions CI/CD

이 실습은 GitHub Actions로 자동 검증을 실행하는 흐름을 다룹니다.

처음에는 복잡한 배포 자동화보다 **코드가 push될 때 Docker image가 build 되는지 자동으로 확인하는 것**을 목표로 합니다.

## workflow 위치

실습 예시 파일:

```text
02_service-deployment-and-automation/04_github-actions-cicd/.github/workflows/docker-build-check.yml
```

실제 GitHub 저장소에서 자동 실행하려면 저장소 루트 기준 아래 위치에 있어야 합니다.

```text
.github/workflows/docker-build-check.yml
```

## 기본 흐름

```text
push 또는 pull request
-> GitHub Actions 실행
-> Python 문법 검사
-> Docker image build
-> 성공/실패 확인
```

## 확인할 것

- workflow 파일 위치가 맞는가?
- push 또는 pull request에서 실행되는가?
- Docker build가 실패하면 어떤 로그가 남는가?
- API Key 같은 비밀 값이 로그에 노출되지 않는가?

## AWS 배포와의 관계

GitHub Actions는 나중에 ECR push, App Runner/ECS 배포까지 확장할 수 있습니다. 이 단원에서는 먼저 자동 검증 흐름을 이해합니다.
