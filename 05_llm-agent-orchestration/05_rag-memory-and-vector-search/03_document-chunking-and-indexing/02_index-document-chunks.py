r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\03_document-chunking-and-indexing

실행 명령:
    python .\02_index-document-chunks.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""문서 chunk를 embedding으로 변환해 pgvector 테이블에 저장하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
CURRENT_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent_user:agent_password@localhost:5433/agent_db")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 chunk indexing을 건너뜁니다.")
    raise SystemExit(0)

sample_path = CURRENT_DIR / "sample_course_guide.md"

if sample_path.exists():
    text = sample_path.read_text(encoding="utf-8")
else:
    # 문서 정리 후 샘플 Markdown 파일이 없어도 indexing 흐름을 실습할 수 있게 합니다.
    text = """
    05 LLM Agent Orchestration 과정은 Prompt, Tool Calling, RAG, Memory, LangGraph를 순서대로 학습합니다.
    학습자는 먼저 LLM 호출 방식을 이해하고, 이후 Python 함수 Tool을 설계합니다.
    RAG 단원에서는 문서를 chunk로 나누고 embedding으로 변환한 뒤 pgvector에 저장합니다.
    LangGraph 단원에서는 Agent의 상태를 State로 관리하고 Node와 Edge로 실행 흐름을 구성합니다.
    Docker Compose와 AWS 배포는 07 과정에서 다룹니다.
    """

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=60)
chunks = splitter.split_text(text)

client = OpenAI()

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM document_chunks WHERE document_title = %s", ("sample_course_guide",))
        for index, chunk in enumerate(chunks):
            response = client.embeddings.create(model=embedding_model, input=chunk)
            embedding = response.data[0].embedding
            cur.execute(
                """
                INSERT INTO document_chunks (document_title, chunk_index, content, embedding)
                VALUES (%s, %s, %s, %s::vector)
                """,
                ("sample_course_guide", index, chunk, str(embedding)),
            )
    conn.commit()

print(f"저장한 chunk 수: {len(chunks)}")
