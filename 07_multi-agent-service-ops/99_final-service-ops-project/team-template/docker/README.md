# Docker

Docker 관련 설정과 확장 문서를 정리하는 영역입니다.

## 확인할 것

- Dockerfile이 필요한 파일을 모두 복사하는가?
- `requirements.txt` 설치가 정상인가?
- `docker-compose.yml`에 backend, frontend, worker, monitor가 모두 정의되어 있는가?
- port와 환경변수가 문서와 일치하는가?

## 기본 명령

```powershell
docker compose config
docker compose up --build
docker compose ps
docker compose logs backend
docker compose down
```
