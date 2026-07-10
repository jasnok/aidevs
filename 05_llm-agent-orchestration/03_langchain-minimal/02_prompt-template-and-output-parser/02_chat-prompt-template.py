r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\02_prompt-template-and-output-parser

실행 명령:
    python .\02_chat-prompt-template.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""ChatPromptTemplate으로 역할 기반 메시지를 만드는 예제입니다."""

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

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 백엔드 입문 수업을 진행하는 튜터다. 답변은 짧고 정확하게 한다."),
        ("human", "{topic}을 실습 관점에서 설명하고 확인 방법도 알려줘."),
    ]
)

chain = prompt | ChatOpenAI(model=model_name) | StrOutputParser()

print(chain.invoke({"topic": "FastAPI health check API"}))
