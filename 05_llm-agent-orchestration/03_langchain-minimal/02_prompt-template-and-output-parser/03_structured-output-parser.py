r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\02_prompt-template-and-output-parser

실행 명령:
    python .\03_structured-output-parser.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""LangChain 모델의 structured output 기능으로 Pydantic 구조를 받는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class StudyPlan(BaseModel):
    """LLM 응답이 따라야 하는 학습 계획 구조입니다."""

    topic: str = Field(description="학습 주제")
    summary: str = Field(description="학습 내용 요약")
    steps: list[str] = Field(description="학습 단계 목록")
    estimated_minutes: int = Field(description="예상 학습 시간")


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 LangChain 모델 호출을 건너뜁니다.")
    raise SystemExit(0)

model = ChatOpenAI(model=model_name)
structured_model = model.with_structured_output(StudyPlan)

result = structured_model.invoke("FastAPI와 Streamlit 연동을 공부하기 위한 짧은 학습 계획을 만들어줘.")

print(result)
print("\n학습 주제:", result.topic)
print("학습 단계:")
for step in result.steps:
    print("-", step)
