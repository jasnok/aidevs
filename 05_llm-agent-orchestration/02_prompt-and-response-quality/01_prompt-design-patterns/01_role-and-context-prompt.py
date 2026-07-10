r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\01_prompt-design-patterns

실행 명령:
    python .\01_role-and-context-prompt.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""역할, 맥락, 작업, 출력 형식을 나누어 프롬프트를 작성하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    print("이 예제는 OpenAI 응답을 비교하는 실습이므로 API Key가 필요합니다.")
    raise SystemExit(0)

client = OpenAI()

# 프롬프트를 한 문장으로 길게 쓰기보다,
# 역할, 맥락, 작업, 출력 형식으로 나누면 모델이 요구사항을 더 안정적으로 이해합니다.
prompt = """
# 역할
너는 Python과 FastAPI를 쉽게 설명하는 튜터다.

# 맥락
학습자는 Python 기초를 막 끝냈고 FastAPI를 처음 배운다.
웹 서버, API, HTTP 개념은 아직 익숙하지 않다.

# 작업
FastAPI의 핵심 개념을 초보자에게 설명해라.

# 출력 형식
- 핵심 요약 3줄
- 쉬운 비유 1개
- 다음에 공부할 키워드 3개
""".strip()

print(f"사용 모델: {model}")
print("[프롬프트]")
print(prompt)

response = client.responses.create(model=model, input=prompt)

print("\n[응답]")
print(response.output_text)
