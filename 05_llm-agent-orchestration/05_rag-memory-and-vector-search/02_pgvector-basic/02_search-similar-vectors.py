r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\02_pgvector-basic

실행 명령:
    python .\02_search-similar-vectors.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""pgvector cosine distance로 비슷한 벡터를 검색하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")
query_vector = "[0.85,0.15,0.25]"

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT title, content, embedding <=> %s::vector AS cosine_distance
            FROM sample_vectors
            ORDER BY embedding <=> %s::vector
            LIMIT 3
            """,
            (query_vector, query_vector),
        )
        rows = cur.fetchall()

for title, content, distance in rows:
    print(f"{title} | distance={distance:.4f} | {content}")
