r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\01_openai-api-basic

실행 명령:
    python .\02_openai-basic-response.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""OpenAI Responses API로 첫 응답을 받아보는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# 이 단원 폴더의 .env 파일을 읽습니다.
BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

# .env에서 API Key와 모델명을 가져옵니다.
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# API Key가 없으면 실제 호출을 하지 않고 안내 메시지만 출력합니다.
# 이렇게 하면 API Key가 없는 환경에서도 예제 파일을 안전하게 실행해 볼 수 있습니다.
if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 OpenAI API 호출을 건너뜁니다.")
    print("로컬 Llama 실습은 02_ollama-docker-llama 폴더에서 진행할 수 있습니다.")
    raise SystemExit(0)

# OpenAI()는 OPENAI_API_KEY 환경 변수를 자동으로 읽어 인증에 사용합니다.
client = OpenAI()

# input에는 모델에게 전달할 사용자 요청을 작성합니다.
prompt = "Python을 처음 배우는 사람에게 API가 무엇인지 세 문장으로 설명해줘."

print(f"사용 모델: {model}")
print("[요청]")
print(prompt)

# Responses API는 OpenAI 모델에 요청을 보내고 응답 객체를 반환합니다.
response = client.responses.create(
    model=model,
    input=prompt,
)

# output_text에는 모델이 생성한 최종 텍스트가 들어 있습니다.
print("\n[응답]")
print(response.output_text)
