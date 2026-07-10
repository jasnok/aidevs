r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\04_debugging-with-langsmith

실행 명령:
    python .\01_tracing-env-check.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""LangSmith tracing 환경 변수 설정 상태를 확인하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

tracing = os.getenv("LANGSMITH_TRACING", "false")
api_key = os.getenv("LANGSMITH_API_KEY", "")
project = os.getenv("LANGSMITH_PROJECT", "aidev-langgraph-practice")

print("LANGSMITH_TRACING:", tracing)
print("LANGSMITH_PROJECT:", project)

if tracing.lower() == "true" and api_key and api_key != "your-langsmith-api-key":
    print("LangSmith tracing을 사용할 준비가 되어 있습니다.")
elif tracing.lower() == "true":
    print("LANGSMITH_TRACING은 true이지만 API Key가 설정되지 않았습니다.")
else:
    print("LangSmith tracing은 비활성화되어 있습니다. 기본 실습에는 문제가 없습니다.")
