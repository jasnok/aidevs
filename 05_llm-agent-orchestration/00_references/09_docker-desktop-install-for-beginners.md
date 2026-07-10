# 09 Docker Desktop Install for Beginners

이 문서는 Docker를 처음 설치하는 입문자를 위한 안내입니다.

05 과정부터는 Docker Desktop을 사용합니다. 하지만 이 과정의 목표는 Docker 운영 전문가가 되는 것이 아닙니다. Docker를 이용해 로컬 Llama, PostgreSQL/pgvector, Redis 같은 실습 도구를 쉽게 실행하는 것이 목표입니다.

## 왜 Docker를 설치하나요?

05 과정에서는 다음 도구를 Docker로 실행합니다.

```text
Ollama 컨테이너
-> 내 PC에서 Llama 모델을 API처럼 호출하기 위해 사용

PostgreSQL + pgvector 컨테이너
-> RAG 실습에서 벡터와 대화 메모리를 저장하기 위해 사용

Redis 컨테이너
-> 세션 메모리와 캐시를 실습하기 위해 사용
```

Docker를 쓰면 개인 환경마다 PC 환경이 조금 달라도 같은 명령으로 같은 실습 환경을 만들 수 있습니다.

## 설치 전에 알아둘 용어

```text
Docker Desktop:
- Windows에서 Docker를 쉽게 실행하게 해주는 프로그램

WSL 2:
- Windows 안에서 Linux 실행 환경을 제공하는 기능
- Docker Desktop은 Windows에서 Linux 컨테이너를 실행할 때 WSL 2를 주로 사용

Image:
- 컨테이너를 만들기 위한 템플릿
- 예: ollama/ollama:latest, pgvector/pgvector:pg16, redis:7

Container:
- Image를 실제로 실행한 것
- 예: ollama-llm, aidev-pgvector, aidev-redis

Volume:
- 컨테이너 밖에 데이터를 보관하는 저장 공간
- 컨테이너를 삭제해도 volume을 지우지 않으면 데이터가 남을 수 있음
```

## 설치 순서

1. Docker 공식 Windows 설치 문서를 엽니다.
2. Docker Desktop Installer를 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 설치 중 WSL 2 안내가 나오면 기본 안내에 따라 진행합니다.
5. 설치가 끝나면 Windows를 재부팅합니다.
6. Docker Desktop을 실행합니다.
7. Docker Desktop이 완전히 실행될 때까지 기다립니다.

공식 문서:

```text
https://docs.docker.com/desktop/setup/install/windows-install/
https://docs.docker.com/desktop/features/wsl/
```

## 설치 후 첫 확인

PowerShell을 열고 아래 명령을 실행합니다.

```powershell
docker --version
docker ps
```

정상이라면 `docker --version`은 Docker 버전을 보여주고, `docker ps`는 실행 중인 컨테이너 목록을 보여줍니다.

처음에는 컨테이너가 없을 수 있습니다. 목록이 비어 있어도 오류가 아니면 정상입니다.

## hello-world 테스트

Docker가 실제로 이미지를 내려받고 컨테이너를 실행할 수 있는지 확인합니다.

```powershell
docker run hello-world
```

처음 실행하면 Docker가 `hello-world` 이미지를 다운로드한 뒤 테스트 메시지를 출력합니다.

이 컨테이너는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않는 것이 정상입니다.

종료된 컨테이너를 확인합니다.

```powershell
docker ps -a
```

필요하면 종료된 컨테이너를 삭제합니다.

```powershell
docker rm 컨테이너ID
```

## 수업 전 체크리스트

- [ ] Docker Desktop이 설치되어 있다.
- [ ] Docker Desktop을 실행할 수 있다.
- [ ] PowerShell에서 `docker --version`이 동작한다.
- [ ] PowerShell에서 `docker ps`가 오류 없이 실행된다.
- [ ] `docker run hello-world`가 성공한다.
- [ ] PC를 재부팅한 뒤에도 Docker Desktop이 다시 실행된다.

## 자주 생기는 상황

### docker 명령을 찾을 수 없다고 나오는 경우

Docker Desktop 설치가 완료되지 않았거나, PowerShell을 설치 전에 열어 둔 상태일 수 있습니다.

해결 순서:

```text
1. Docker Desktop이 설치되어 있는지 확인
2. Docker Desktop 실행
3. PowerShell을 닫고 다시 열기
4. docker --version 다시 실행
5. 그래도 안 되면 PC 재부팅
```

### docker ps에서 Docker daemon 오류가 나오는 경우

Docker Desktop이 아직 실행되지 않았거나, Docker Engine이 시작 중일 수 있습니다.

해결 순서:

```text
1. Docker Desktop 실행
2. 상태가 정상 실행될 때까지 기다림
3. PowerShell에서 docker ps 다시 실행
4. 계속 실패하면 Docker Desktop 재시작
5. 그래도 실패하면 PC 재부팅
```

### WSL 관련 오류가 나오는 경우

Windows에서 Docker Desktop은 WSL 2 기반으로 동작하는 경우가 많습니다.

확인 명령:

```powershell
wsl --status
wsl --list --verbose
```

WSL 2가 준비되지 않았다는 메시지가 나오면 Docker 공식 WSL 문서를 확인하고, Windows 업데이트와 WSL 설치 상태를 먼저 점검합니다.

## 05 과정에서 Docker를 사용하는 범위

05에서는 아래까지만 다룹니다.

```text
docker --version
docker ps
docker run
docker exec
docker stop
docker start
docker rm
docker volume rm
```

아래 내용은 07 과정에서 다룹니다.

```text
Dockerfile
Docker Compose
Health Check
Restart Policy
AWS 배포
GitHub Actions
서비스 운영 자동화
```

## 직접 기억할 문장

```text
05에서 Docker는 운영 배포 도구가 아니라, 로컬 실습 도구입니다.
설치 후 docker ps가 정상 동작하면 05 수업을 시작할 준비가 된 것입니다.
```
