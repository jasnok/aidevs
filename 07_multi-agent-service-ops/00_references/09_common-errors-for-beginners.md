# 69. Common Errors For Beginners

07 과정에서 자주 만나는 오류와 확인 방법입니다.

## PowerShell 실행 정책 오류

증상:

```text
running scripts is disabled on this system
```

해결:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Docker 명령을 찾을 수 없음

확인:

```powershell
docker --version
```

해결:

- Docker Desktop 설치 여부 확인
- 설치 후 PowerShell 재시작
- Windows 재부팅

## Docker Desktop은 켰는데 `docker ps`가 실패함

확인:

```powershell
docker ps
```

해결:

- Docker Desktop이 완전히 실행될 때까지 기다립니다.
- WSL 관련 안내가 나오면 Docker Desktop 안내에 따라 설정합니다.

## `.env` 파일이 없음

해결:

```powershell
Copy-Item .env.example .env
```

## Docker Compose 문법 오류

확인:

```powershell
docker compose config
```

자주 보는 원인:

- 들여쓰기 오류
- 포트 형식 오류
- `.env` 파일 누락
- service 이름 오타

## 포트 충돌

증상:

```text
port is already allocated
```

확인:

```powershell
docker ps
```

해결:

```powershell
docker stop <container_id>
```

또는 `docker-compose.yml`에서 포트를 변경합니다.

## Docker image build 실패

확인:

```powershell
docker build --no-cache -t aidev-agent-backend:local .
```

자주 보는 원인:

- `requirements.txt` 파일 누락
- Dockerfile의 `COPY` 경로 오류
- Python 패키지 설치 실패
- 실행 명령 오타

## AWS 비용 걱정

AWS 배포 실습은 필수입니다. 배포를 완료한 뒤에는 App Runner, ECR, CloudWatch 리소스를 정리하고 Billing Dashboard에서 비용을 확인합니다.

확인할 리소스:

- App Runner Service
- ECS Service
- Load Balancer
- ECR image
- CloudWatch Log Group
