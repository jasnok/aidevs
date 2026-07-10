# 90 AI-assisted Agent Review and Debugging

이 단원은 05 과정 실습 중 자주 막히는 지점을 AI와 함께 점검하는 참고 단원입니다.

Agent 실습은 OpenAI API, Docker, PostgreSQL/pgvector, Redis, LangGraph, Tool 호출이 함께 등장하기 때문에 오류 원인을 한 번에 찾기 어렵습니다. 이 폴더에서는 오류를 종류별로 나누고, 어떤 정보를 AI에게 전달해야 빠르게 도움을 받을 수 있는지 정리합니다.

## 폴더 구성

```text
90_ai-assisted-agent-review-and-debugging
├─ README.md
├─ 01_docker-run-troubleshooting.md
├─ 02_openai-ollama-errors.md
├─ 03_pgvector-redis-errors.md
├─ 04_langgraph-state-errors.md
├─ 05_tool-mcp-errors.md
└─ 06_ai-code-review-checklist.md
```

## 먼저 확인할 것

```text
1. 현재 폴더 위치
2. 활성화된 Python 가상환경
3. .env 파일 위치
4. docker ps 결과
5. 실행한 정확한 명령어
6. 전체 오류 메시지
```

## AI에게 질문할 때 포함할 정보

```text
나는 C:\aidev\05_llm-agent-orchestration\... 폴더에서 실습 중이다.
실행한 명령어는 ... 이다.
기대 결과는 ... 이다.
실제 오류 메시지는 ... 이다.
관련 파일은 ... 이다.
Docker 컨테이너 상태는 docker ps 결과 ... 이다.
```

## 이 단원의 목표

- 오류 메시지를 무작정 복사하지 않고 원인 후보를 나누어 본다.
- Docker, API Key, DB 연결, Redis 연결, LangGraph State 오류를 구분한다.
- AI에게 재현 가능한 정보를 전달하는 습관을 만든다.
- 최종 프로젝트 전에 코드 리뷰 체크리스트를 사용해 위험한 부분을 먼저 점검한다.
