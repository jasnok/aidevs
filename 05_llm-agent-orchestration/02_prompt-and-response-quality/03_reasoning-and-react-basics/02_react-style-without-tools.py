r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\03_reasoning-and-react-basics

실행 명령:
    python .\02_react-style-without-tools.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""도구 호출 없이 ReAct 흐름을 개념적으로 연습하는 예제입니다."""

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

# 실제 Tool은 아직 호출하지 않습니다.
# 04_function-calling-and-tool-use 단원으로 가기 전에,
# 어떤 상황에서 어떤 도구가 필요한지 판단하는 흐름만 연습합니다.
prompt = """
사용자 요청:
이번 주 학습 로그를 분석해서 가장 어려워한 주제를 찾아줘.

사용 가능한 가상 도구:
- get_learning_logs: 학습 로그 목록 조회
- summarize_logs: 로그 요약
- create_action_plan: 보충 학습 계획 생성

아래 형식으로만 답하라.

요청 이해: 한 문장
필요한 도구 순서: 도구 이름을 순서대로 나열
각 도구를 쓰는 이유: 짧게 설명
최종 응답 예시: 사용자에게 보여줄 말
""".strip()

print(f"사용 모델: {model}")
print("[프롬프트]")
print(prompt)

response = client.responses.create(model=model, input=prompt)

print("\n[응답]")
print(response.output_text)
