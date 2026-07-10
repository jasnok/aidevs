r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\03_reasoning-and-react-basics

실행 명령:
    python .\01_plan-act-review-pattern.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""계획-실행-검토 구조로 응답을 안정화하는 예제입니다."""

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

# 이 예제는 숨겨진 내부 사고 과정을 출력하게 하는 것이 목적이 아닙니다.
# 사용자가 볼 수 있는 작업 계획, 위험 요소, 확인 방법을 정리하게 합니다.
prompt = """
수강생이 FastAPI와 Streamlit을 연결하는 미니 프로젝트를 시작하려고 한다.

아래 형식으로 답하라.

1. 작업 계획: 5단계 이내
2. 먼저 만들 파일: 파일명과 역할
3. 위험 요소: 초보자가 자주 실수하는 점 3개
4. 최종 확인 방법: 실행과 검증 방법

내부 사고 과정은 출력하지 말고, 실무자가 바로 볼 수 있는 결과만 작성하라.
""".strip()

print(f"사용 모델: {model}")
print("[프롬프트]")
print(prompt)

response = client.responses.create(model=model, input=prompt)

print("\n[응답]")
print(response.output_text)
