r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\03_chain-and-runnable

실행 명령:
    python .\02_batch-and-stream.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""batch와 stream 실행 방식을 확인하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 LangChain 모델 호출을 건너뜁니다.")
    raise SystemExit(0)

prompt = ChatPromptTemplate.from_template("{topic}을 초보자에게 한 문장으로 설명해줘.")
chain = prompt | ChatOpenAI(model=model_name) | StrOutputParser()

# batch는 여러 입력을 같은 체인으로 처리할 때 사용합니다.
results = chain.batch(
    [
        {"topic": "FastAPI"},
        {"topic": "Streamlit"},
        {"topic": "PostgreSQL"},
    ]
)

print("[batch 결과]")
for result in results:
    print("-", result)

print("\n[stream 결과]")
for chunk in chain.stream({"topic": "LangChain streaming"}):
    print(chunk, end="", flush=True)
print()
