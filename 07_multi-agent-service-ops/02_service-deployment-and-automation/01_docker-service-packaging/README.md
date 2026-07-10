# 01 Docker Service Packaging

이 실습은 Python FastAPI 서비스를 Docker image로 패키징하고 실행하는 방법을 다룹니다.

## Dockerfile 흐름

```text
Python 기본 이미지 선택
-> 작업 폴더 생성
-> requirements.txt 복사
-> 패키지 설치
-> app 코드 복사
-> 실행 명령 지정
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## 확인할 것

- Docker image가 정상 build 되는가?
- container가 8000 포트로 실행되는가?
- `/health`가 정상 응답하는가?
- `Ctrl + C`로 종료할 수 있는가?
