r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\01_embedding-basics

실행 명령:
    python .\02_openai-embedding-basic.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""OpenAI Embedding API로 텍스트를 벡터로 바꾸는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 Embedding API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

text = "FastAPI는 Python으로 API 서버를 만들 때 사용하는 웹 프레임워크입니다."
response = client.embeddings.create(model=embedding_model, input=text)
embedding = response.data[0].embedding

print("embedding dimension:", len(embedding))
print("first 10 values:", embedding[:10])
