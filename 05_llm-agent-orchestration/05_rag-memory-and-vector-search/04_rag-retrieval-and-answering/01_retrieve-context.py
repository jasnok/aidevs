r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\04_rag-retrieval-and-answering

실행 명령:
    python .\01_retrieve-context.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""질문과 관련 있는 문서 chunk를 pgvector로 검색하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 검색을 건너뜁니다.")
    raise SystemExit(0)

question = "LLM Agent 과정에서는 무엇을 배우나요?"
client = OpenAI()
embedding = client.embeddings.create(model=embedding_model, input=question).data[0].embedding

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT content, embedding <=> %s::vector AS distance
            FROM document_chunks
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> %s::vector
            LIMIT 3
            """,
            (str(embedding), str(embedding)),
        )
        rows = cur.fetchall()

print("질문:", question)
for index, (content, distance) in enumerate(rows, start=1):
    print(f"\n--- 검색 결과 {index} | distance={distance:.4f} ---")
    print(content)
