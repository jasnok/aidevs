# Team Template

이 폴더는 Docker Compose 기반 Auto Healing Multi-Agent 서비스 프로젝트 템플릿입니다.

## 서비스 구성

| 서비스 | 역할 |
| --- | --- |
| backend | FastAPI API 서버, Agent 실행 상태 제공 |
| frontend | Streamlit 사용자 화면 |
| worker | Auto Healing 작업 실행기 |
| monitor | 운영 상태와 이벤트 확인 화면 |

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\team-template
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인 주소

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

## 종료

```powershell
docker compose down
```

## 프로젝트 확장 기준

- 장애 시나리오를 2개 이상 추가합니다.
- Agent 역할을 명확히 나눕니다.
- retry/restart/fallback 기준을 문서화합니다.
- 정책 위반 또는 권한 위반 로그를 남깁니다.
- monitor 화면에서 운영 상태를 확인할 수 있게 합니다.
