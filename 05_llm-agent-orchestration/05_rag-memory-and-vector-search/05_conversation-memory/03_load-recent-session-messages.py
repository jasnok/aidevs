r"""PostgreSQL에서 특정 세션의 최근 대화만 불러오는 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search

실행 명령:
    python .\05_conversation-memory\03_load-recent-session-messages.py

필요한 준비:
    1. aidev-pgvector 컨테이너가 실행 중이어야 합니다.
    2. 02_pgvector-basic/01_create-extension-and-tables.sql을 먼저 적용해야 합니다.
    3. 02_save-conversation-memory.py를 한 번 실행해 샘플 대화를 저장하면 결과를 보기 쉽습니다.

이 예제의 목적:
    Agent가 매번 모든 대화를 읽는 대신, 현재 session_id의 최근 N개 메시지만
    읽어서 짧은 대화 맥락으로 사용하는 흐름을 이해합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://agent_user:agent_password@localhost:5433/agent_db",
)

SESSION_ID = "demo-session-001"
LIMIT = 5


def load_recent_messages(session_id: str, limit: int) -> list[tuple[str, str, str]]:
    """최근 대화를 오래된 순서로 반환합니다."""
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT role, content, created_at
                FROM conversation_messages
                WHERE session_id = %s
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (session_id, limit),
            )
            rows = cur.fetchall()

    # DB에서는 최신순으로 가져왔지만, 프롬프트에 넣을 때는 오래된 순서가 읽기 쉽습니다.
    rows.reverse()
    return rows


def main() -> None:
    print("PostgreSQL Session Memory 조회")
    print("session_id:", SESSION_ID)
    print("limit:", LIMIT)

    messages = load_recent_messages(SESSION_ID, LIMIT)

    if not messages:
        print("\n저장된 대화가 없습니다.")
        print("먼저 python .\\05_conversation-memory\\02_save-conversation-memory.py 를 실행해 보세요.")
        return

    print("\n최근 대화:")
    for role, content, created_at in messages:
        print(f"- [{created_at}] {role}: {content}")


if __name__ == "__main__":
    main()
