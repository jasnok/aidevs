r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\04_debugging-with-langsmith

실행 명령:
    python .\02_planning-tracing-evaluation.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Planning, Tracing, Evaluation을 한 번에 이해하는 mock 예제입니다.

LangSmith를 실제로 연결하기 전에, 에이전트 실행을 어떤 관점으로 기록하고
평가해야 하는지 먼저 확인합니다.
"""


PLAN = [
    "1. 사용자 요청 의도 파악",
    "2. 필요한 도구 또는 RAG 검색 선택",
    "3. 검색 결과와 세션 기억을 합쳐 답변 생성",
    "4. 답변 품질 평가",
]

TRACE_EVENTS = [
    {"step": "route", "status": "ok", "detail": "RAG 검색이 필요하다고 판단"},
    {"step": "retrieve", "status": "ok", "detail": "관련 문서 2개 검색"},
    {"step": "answer", "status": "ok", "detail": "검색 근거 기반 답변 생성"},
    {"step": "evaluate", "status": "warning", "detail": "출처 표시가 부족함"},
]

EVALUATION = {
    "groundedness": 1,
    "answer_completeness": 1,
    "source_clarity": 0,
}


print("Planning")
print("-" * 40)
for item in PLAN:
    print(item)

print("\nTracing")
print("-" * 40)
for event in TRACE_EVENTS:
    print(f"{event['step']} | {event['status']} | {event['detail']}")

print("\nEvaluation")
print("-" * 40)
for key, score in EVALUATION.items():
    print(f"{key}: {score}")

print("\n개선 제안")
print("-" * 40)
if EVALUATION["source_clarity"] == 0:
    print("답변에 어떤 문서를 근거로 사용했는지 출처 표시를 추가합니다.")
else:
    print("현재 답변 품질 기준을 통과했습니다.")
