# 06 AI Code Review Checklist

최종 프로젝트 전에 아래 항목을 점검합니다.

## 보안

- [ ] `.env` 파일을 제출하지 않는다.
- [ ] API Key를 코드에 직접 쓰지 않는다.
- [ ] 오류 메시지에 민감 정보가 노출되지 않는다.

## Docker

- [ ] `docker ps`로 필요한 컨테이너를 확인했다.
- [ ] 포트와 `.env` URL이 일치한다.
- [ ] Docker Compose를 05 과정 필수 실습으로 사용하지 않는다.

## Tool

- [ ] Tool은 하나의 책임만 가진다.
- [ ] Tool 입력과 출력이 문서화되어 있다.
- [ ] 실패 시 Fallback이 있다.

## Memory and RAG

- [ ] Session Memory와 Long-term Memory 역할이 구분된다.
- [ ] pgvector 검색 결과가 최종 답변에 어떻게 사용되는지 설명할 수 있다.
- [ ] RAG 답변의 근거성을 평가했다.

## LangGraph

- [ ] State 필드가 명확하다.
- [ ] Node 책임이 분리되어 있다.
- [ ] Edge 흐름이 그림이나 표로 설명되어 있다.
- [ ] Retry 또는 Self-Reflection 조건이 무한 반복을 만들지 않는다.
