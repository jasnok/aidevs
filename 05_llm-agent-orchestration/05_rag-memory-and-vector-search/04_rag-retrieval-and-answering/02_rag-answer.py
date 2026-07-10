r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\04_rag-retrieval-and-answering

실행 명령:
    python .\02_rag-answer.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""검색된 context를 사용해 RAG 답변을 생성하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
chat_model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 RAG 답변 생성을 건너뜁니다.")
    raise SystemExit(0)

question = "LLM Agent 과정에서는 RAG를 어떻게 배우나요?"
client = OpenAI()
query_embedding = client.embeddings.create(model=embedding_model, input=question).data[0].embedding

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT content
            FROM document_chunks
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> %s::vector
            LIMIT 3
            """,
            (str(query_embedding),),
        )
        contexts = [row[0] for row in cur.fetchall()]

context_text = "\n\n".join(contexts)

prompt = f"""
너는 수업 안내 도우미다.
아래 context에 있는 내용만 근거로 답하라.
context에 없는 내용은 모른다고 말하라.

# context
{context_text}

# 질문
{question}
""".strip()

response = client.responses.create(model=chat_model, input=prompt)
print(response.output_text)
