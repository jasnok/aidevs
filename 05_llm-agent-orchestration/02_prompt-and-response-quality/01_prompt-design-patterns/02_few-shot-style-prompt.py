r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\01_prompt-design-patterns

실행 명령:
    python .\02_few-shot-style-prompt.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""예시를 제공해서 원하는 답변 스타일을 유도하는 예제입니다."""

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
    raise SystemExit(0)

client = OpenAI()

# Few-shot은 예시를 먼저 보여준 뒤 실제 요청을 보내는 방식입니다.
# 모델은 예시의 형식과 말투를 참고해 실제 입력에도 비슷하게 답하려고 합니다.
prompt = """
너는 개발 입문자를 위한 용어 설명 도우미다.
아래 예시처럼 짧고 쉽게 설명해라.

예시 입력: 변수
예시 출력:
개념: 값을 담아두는 이름이다.
비유: 이름표가 붙은 상자와 비슷하다.
예시: age = 20

예시 입력: 함수
예시 출력:
개념: 자주 쓰는 코드를 이름 붙여 묶어둔 것이다.
비유: 버튼을 누르면 정해진 일이 실행되는 기계와 비슷하다.
예시: greet()

실제 입력: API
""".strip()

print(f"사용 모델: {model}")
print("[프롬프트]")
print(prompt)

response = client.responses.create(model=model, input=prompt)

print("\n[응답]")
print(response.output_text)
