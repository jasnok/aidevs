# 08 Final Project Roadmap

`99_final-agent-project`는 이 과정의 마무리 프로젝트입니다.

## 기본 주제

```text
복합 API 연계 일정 조정 에이전트
```

사용자 요청 예시:

```text
Kim, Lee, Park이 모두 가능한 30분 회의 시간을 찾아서 제안 메시지를 만들어줘.
```

## 프로젝트에서 사용하는 개념

| 과정 내용 | 프로젝트 적용 |
| --- | --- |
| OpenAI API | 자연스러운 메시지 생성 |
| Prompt | 일정 제안 답변 형식 설계 |
| LangChain | 모델 호출 구조화 |
| Function Calling | 일정 조회, 후보 계산 도구 설계 |
| MCP | 외부 도구 연결 표준화 개념 이해 |
| RAG | 회의 정책 또는 문서 검색 |
| Memory | 이전 요청이나 결정 이력 저장 |
| Self-Reflection | 답변 품질 검토와 수정 루프 |
| LangGraph | 전체 에이전트 흐름 관리 |

## 추천 에이전트 흐름

```text
START
-> analyze_request
-> select_tool
-> execute_tool
-> retrieve_policy_context
-> generate_candidate_message
-> review_answer
-> END
```

## 팀 프로젝트 최소 기준

- LangGraph 노드 3개 이상
- Tool 함수 2개 이상
- Tool 선택 기준과 Fallback 전략
- Self-Reflection 또는 답변 검토 단계
- Streamlit UI 1개 이상
- 사용자 요청 입력 기능
- 최종 답변 출력 기능
- README 실행 방법 정리
- 발표 자료 작성

## 확장 아이디어

### 학습 코치 에이전트

- 학습 로그 조회
- 어려운 주제 분석
- 보충 학습 계획 생성

### 문서 Q&A 에이전트

- 수업 자료 chunking
- pgvector 검색
- 근거 기반 답변 생성

### 고객 문의 분류 에이전트

- 문의 유형 분류
- 우선순위 판단
- 담당 부서 추천

### 일정 조정 에이전트

- 참석자 추출
- 가능 시간 조회
- 회의 후보 추천
- 안내 메시지 생성

## 발표 때 보여줄 것

1. 사용자의 문제
2. 에이전트 흐름도
3. State 구조
4. Tool 목록
5. 실행 화면
6. 최종 답변 예시
7. 어려웠던 점
8. 개선 방향

## 배포 범위

05 과정에서는 로컬 실행과 Agent 흐름 검증을 우선합니다.

Docker Compose, Render/AWS 배포, GitHub Actions 자동화, 장애 대응은 `07_multi-agent-service-ops`에서 확장합니다.
