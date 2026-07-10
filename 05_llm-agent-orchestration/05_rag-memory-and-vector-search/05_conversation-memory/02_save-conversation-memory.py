r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\05_conversation-memory

실행 명령:
    python .\02_save-conversation-memory.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Docker run으로 실행한 pgvector PostgreSQL에 대화 메시지를 저장하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

# 05 과정에서는 PostgreSQL을 PC에 직접 설치하지 않습니다.
# 아래 기본 주소는 docker run으로 실행한 aidev-pgvector 컨테이너를 가리킵니다.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")

session_id = "demo-session-001"
messages = [
    ("user", "LLM Agent 과정에서는 무엇을 배우나요?"),
    ("assistant", "OpenAI API, LangChain, Function Calling, RAG, LangGraph를 배웁니다."),
]

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        for role, content in messages:
            cur.execute(
                """
                INSERT INTO conversation_messages (session_id, role, content)
                VALUES (%s, %s, %s)
                """,
                (session_id, role, content),
            )
        cur.execute(
            """
            SELECT role, content, created_at
            FROM conversation_messages
            WHERE session_id = %s
            ORDER BY id
            """,
            (session_id,),
        )
        rows = cur.fetchall()
    conn.commit()

for role, content, created_at in rows:
    print(f"[{created_at}] {role}: {content}")
