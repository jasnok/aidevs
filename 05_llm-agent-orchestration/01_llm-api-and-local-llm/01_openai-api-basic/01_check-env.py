r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\01_openai-api-basic

실행 명령:
    python .\01_check-env.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""OpenAI API Key 환경 변수를 확인하는 예제입니다.

이 파일은 실제 OpenAI API를 호출하지 않습니다.
API Key 값을 화면에 직접 출력하지 않고, 설정 여부만 확인합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# 현재 파일은 01_openai-api-basic 폴더 안에 있습니다.
# parents[1]은 그 한 단계 위인 01_llm-api-and-local-llm 폴더를 의미합니다.
BASE_DIR = Path(__file__).resolve().parents[1]

# 이 단원에서 사용하는 .env 파일은 단원 폴더 바로 아래에 있습니다.
ENV_PATH = BASE_DIR / ".env"

# .env 파일의 값을 현재 Python 프로그램의 환경 변수로 읽어옵니다.
# .env 파일이 없어도 프로그램이 바로 실패하지는 않습니다.
load_dotenv(ENV_PATH)

# API Key는 비밀번호처럼 다루어야 합니다.
# 그래서 실제 값을 출력하지 않고, 값이 있는지만 확인합니다.
api_key = os.getenv("OPENAI_API_KEY")

# 모델명은 .env에 없으면 기본값으로 gpt-4.1-mini를 사용합니다.
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

print(f".env 파일 경로: {ENV_PATH}")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 아직 설정되지 않았습니다.")
    print(".env.example 파일을 .env로 복사한 뒤 실제 API Key를 입력하세요.")
    print("API Key가 없어도 Docker/Ollama/Llama 실습은 진행할 수 있습니다.")
else:
    print("OPENAI_API_KEY가 설정되어 있습니다.")
    print(f"사용할 모델: {model}")
