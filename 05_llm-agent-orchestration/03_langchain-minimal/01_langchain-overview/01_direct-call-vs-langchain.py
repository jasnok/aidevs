r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\01_langchain-overview

실행 명령:
    python .\01_direct-call-vs-langchain.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""직접 문자열 처리와 LangChain 체인 구조를 비교하는 예제입니다."""

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

# ChatPromptTemplate은 system, human 역할을 나누어 프롬프트를 구성합니다.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 Python 초보자를 돕는 친절한 튜터다."),
        ("human", "{topic}을 초보자에게 세 문장으로 설명해줘."),
    ]
)

# ChatOpenAI는 LangChain에서 OpenAI 채팅 모델을 호출하는 클래스입니다.
model = ChatOpenAI(model=model_name)

# StrOutputParser는 모델 응답 객체에서 문자열 결과를 꺼내기 쉽게 해줍니다.
parser = StrOutputParser()

# LCEL에서는 | 연산자로 실행 단계를 연결합니다.
chain = prompt | model | parser

result = chain.invoke({"topic": "LangChain"})
print(result)
