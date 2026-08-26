"""연결 확인부터 색인·검색·Cache·LLM 답변까지 전체 RAG Pipeline을 실행합니다."""

import httpx

from _rag_backend import PROVIDER, print_help, request


if __name__ == "__main__":
    try:
        print("1. 인프라 상태", request("GET", "/api/rag/status"))
        print("2. pgvector 색인", request("POST", "/api/rag/index", {"reset_collection": True}))
        result = request("POST", "/api/rag/answer", {
            "query": "바다 박물관은 화요일에 운영하나요?",
            "mode": "pgvector",
            "top_k": 3,
            "provider": PROVIDER,
            "use_cache": True,
        })
        # Trace를 보면 Retrieval과 Generation, Cache 저장 순서를 분리해 확인할 수 있습니다.
        for index, item in enumerate(result["trace"], start=1):
            print(f"{index}. {item['stage']} → {item['data']}")
        print("3. 최종 답변", result["answer"])
        print("4. 출처", result["sources"])
    except httpx.HTTPError as error:
        print_help(error)
