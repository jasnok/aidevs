r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\01_openai-api-basic

실행 명령:
    python .\03_openai-message-style.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""역할을 나누어 LLM에게 요청하는 예제입니다.

단순 문자열 하나를 보내는 방식과 달리, role을 나누면 모델에게
어떤 태도와 기준으로 답해야 하는지 더 분명하게 전달할 수 있습니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 OpenAI API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

# system 역할은 모델의 답변 기준을 정합니다.
# 예: 친절하게 설명하기, 짧게 답하기, 특정 관점으로 답하기
system_message = "너는 Python 입문자를 돕는 친절한 튜터다. 답변은 쉽고 짧게 작성한다."

# user 역할은 실제 사용자의 질문입니다.
user_message = "환경 변수를 사용하는 이유를 예시와 함께 설명해줘."

print(f"사용 모델: {model}")
print("[system]")
print(system_message)
print("\n[user]")
print(user_message)

response = client.responses.create(
    model=model,
    input=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
)

print("\n[assistant]")
print(response.output_text)
