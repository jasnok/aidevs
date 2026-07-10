r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\02_pgvector-basic

실행 명령:
    python .\01_insert-sample-vectors.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""pgvector 테이블에 작은 샘플 벡터를 저장하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")

samples = [
    ("FastAPI", "Python API backend framework", "[0.9,0.1,0.2]"),
    ("Backend", "Server API database logic", "[0.8,0.2,0.3]"),
    ("Streamlit", "Python frontend dashboard", "[0.1,0.9,0.2]"),
]

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM sample_vectors")
        for title, content, embedding in samples:
            cur.execute(
                """
                INSERT INTO sample_vectors (title, content, embedding)
                VALUES (%s, %s, %s::vector)
                """,
                (title, content, embedding),
            )
    conn.commit()

print("샘플 벡터 저장 완료")
