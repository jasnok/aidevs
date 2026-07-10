r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\04_rag-retrieval-and-answering

실행 명령:
    python .\03_hybrid-search-rrf.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""키워드 검색과 벡터 검색 결과를 RRF로 결합하는 개념 예제입니다.

실제 서비스에서는 키워드 검색 결과와 pgvector 검색 결과가 따로 나올 수 있습니다.
Hybrid Search는 두 결과를 합쳐 더 좋은 검색 순위를 만드는 전략입니다.

RRF(Reciprocal Rank Fusion)는 여러 검색 순위에서 높은 위치에 자주 등장한 문서를
더 중요하게 보는 간단한 점수 결합 방식입니다.
"""


KEYWORD_RESULTS = [
    {"doc_id": "doc-a", "title": "LangGraph 상태 흐름"},
    {"doc_id": "doc-b", "title": "RAG 문서 chunking"},
    {"doc_id": "doc-c", "title": "Prompt Injection 방어"},
]

VECTOR_RESULTS = [
    {"doc_id": "doc-b", "title": "RAG 문서 chunking"},
    {"doc_id": "doc-d", "title": "pgvector 검색 구조"},
    {"doc_id": "doc-a", "title": "LangGraph 상태 흐름"},
]


def calculate_rrf_score(rank: int, k: int = 60) -> float:
    """RRF 점수를 계산합니다."""

    return 1 / (k + rank)


def merge_with_rrf(result_lists: list[list[dict[str, str]]]) -> list[dict[str, object]]:
    """여러 검색 결과 목록을 RRF 점수로 합칩니다."""

    scores: dict[str, float] = {}
    titles: dict[str, str] = {}

    for results in result_lists:
        for rank, item in enumerate(results, start=1):
            doc_id = item["doc_id"]
            titles[doc_id] = item["title"]
            scores[doc_id] = scores.get(doc_id, 0) + calculate_rrf_score(rank)

    ranked_items = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return [
        {"doc_id": doc_id, "title": titles[doc_id], "rrf_score": score}
        for doc_id, score in ranked_items
    ]


merged_results = merge_with_rrf([KEYWORD_RESULTS, VECTOR_RESULTS])

print("Hybrid Search 결과")
print("-" * 40)
for index, item in enumerate(merged_results, start=1):
    print(f"{index}. {item['doc_id']} | {item['title']} | score={item['rrf_score']:.5f}")
