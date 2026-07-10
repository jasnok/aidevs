r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\01_embedding-basics

실행 명령:
    python .\01_vector-similarity-basic.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""외부 API 없이 벡터 유사도 개념을 이해하는 예제입니다."""

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """두 벡터의 cosine similarity를 계산합니다."""
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (norm_a * norm_b)


fastapi_vector = [0.9, 0.1, 0.2]
backend_vector = [0.8, 0.2, 0.3]
streamlit_vector = [0.1, 0.9, 0.2]

print("FastAPI vs Backend:", cosine_similarity(fastapi_vector, backend_vector))
print("FastAPI vs Streamlit:", cosine_similarity(fastapi_vector, streamlit_vector))
