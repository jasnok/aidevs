r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\04_rag-retrieval-and-answering

실행 명령:
    python .\04_rag-quality-evaluation.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""RAG 답변 품질을 수동 평가표로 점검하는 예제입니다.

RAGAS 같은 평가 도구를 쓰기 전, 초보자는 먼저 평가 기준을 이해해야 합니다.
이 예제는 API 호출 없이 질문, 검색 context, 답변을 보고 점수를 매기는 방식입니다.
"""


EVALUATION_CASE = {
    "question": "05 과정에서 pgvector는 왜 사용하나요?",
    "context": [
        "pgvector는 PostgreSQL에서 벡터를 저장하고 검색할 수 있게 해주는 확장입니다.",
        "05 과정에서는 docker run으로 PostgreSQL + pgvector 컨테이너를 실행해 RAG 검색을 실습합니다.",
    ],
    "answer": "pgvector는 문서 chunk의 embedding을 저장하고, 질문과 비슷한 chunk를 검색하기 위해 사용합니다.",
}


RUBRIC = {
    "context_relevance": "검색된 context가 질문과 관련 있는가?",
    "groundedness": "답변이 context에 있는 근거를 벗어나지 않는가?",
    "answer_completeness": "질문에 충분히 답하고 있는가?",
}


def score_case(case: dict[str, object]) -> dict[str, int]:
    """간단한 규칙으로 RAG 답변을 평가합니다."""

    question = str(case["question"])
    context_text = " ".join(case["context"])
    answer = str(case["answer"])

    return {
        "context_relevance": 1 if "pgvector" in context_text and "pgvector" in question else 0,
        "groundedness": 1 if "embedding" in answer or "벡터" in answer else 0,
        "answer_completeness": 1 if "저장" in answer and "검색" in answer else 0,
    }


scores = score_case(EVALUATION_CASE)

print("RAG 품질 평가")
print("-" * 40)
print("질문:", EVALUATION_CASE["question"])
print("답변:", EVALUATION_CASE["answer"])
print()

for key, description in RUBRIC.items():
    print(f"{key}: {scores[key]}점 | {description}")

total = sum(scores.values())
print(f"\n총점: {total} / {len(RUBRIC)}")
