r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\02_structured-output-json

실행 명령:
    python .\01_json-output-request.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""프롬프트로 JSON 형식 응답을 요청하는 예제입니다."""

from pathlib import Path
import json
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

# JSON 형식을 요청하면 모델 응답을 Python dict로 바꿔서 처리하기 쉬워집니다.
# 다만 프롬프트만으로는 모델이 항상 완벽한 JSON을 준다고 보장할 수 없습니다.
prompt = """
아래 학습 소감을 분석해서 JSON으로만 답해라.

학습 소감:
오늘 FastAPI 실습은 어렵지만 재미있었고, Docker는 아직 헷갈린다.

JSON 형식:
{
  "summary": "한 문장 요약",
  "sentiment": "positive | neutral | negative",
  "keywords": ["키워드1", "키워드2"],
  "difficulty": 1
}

주의:
- JSON 이외의 설명 문장을 추가하지 마라.
- difficulty는 1부터 5 사이의 숫자로 작성해라.
""".strip()

print(f"사용 모델: {model}")
print("[프롬프트]")
print(prompt)

response = client.responses.create(model=model, input=prompt)
text = response.output_text

print("\n[모델 원본 응답]")
print(text)

# 모델이 준 텍스트를 실제 JSON으로 파싱할 수 있는지 확인합니다.
try:
    parsed = json.loads(text)
except json.JSONDecodeError as exc:
    print("\nJSON 파싱에 실패했습니다.")
    print("이런 상황 때문에 Structured Output 또는 Pydantic 검증이 필요합니다.")
    print(f"오류 내용: {exc}")
else:
    print("\nJSON 파싱 성공")
    print(f"summary: {parsed.get('summary')}")
    print(f"sentiment: {parsed.get('sentiment')}")
    print(f"keywords: {parsed.get('keywords')}")
    print(f"difficulty: {parsed.get('difficulty')}")
