r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\02_structured-output-json

실행 명령:
    python .\02_structured-output-pydantic.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Pydantic 모델로 Structured Output을 받는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


class LearningFeedback(BaseModel):
    """LLM 응답이 따라야 할 구조를 Python 코드로 정의합니다."""

    summary: str = Field(description="학습 피드백 한 문장 요약")
    sentiment: str = Field(description="positive, neutral, negative 중 하나")
    keywords: list[str] = Field(description="핵심 키워드 목록")
    difficulty: int = Field(description="학습 난이도. 1부터 5까지")


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

learning_note = "오늘 FastAPI 실습은 어렵지만 재미있었고, Docker는 아직 헷갈린다."

print(f"사용 모델: {model}")
print("[분석할 문장]")
print(learning_note)

# responses.parse는 모델 응답을 Pydantic 모델 구조에 맞춰 받는 방식입니다.
# 성공하면 response.output_parsed에 LearningFeedback 객체가 들어 있습니다.
response = client.responses.parse(
    model=model,
    input=f"다음 학습 소감을 분석해라: {learning_note}",
    text_format=LearningFeedback,
)

feedback = response.output_parsed

print("\n[Pydantic 객체]")
print(feedback)

print("\n[필드별 출력]")
print("요약:", feedback.summary)
print("감정:", feedback.sentiment)
print("키워드:", ", ".join(feedback.keywords))
print("난이도:", feedback.difficulty)
