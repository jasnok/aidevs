r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\02_ollama-docker-llama

실행 명령:
    python .\01_ollama-health-check.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Ollama 서버가 실행 중인지 확인하는 예제입니다.

OpenAI API는 인터넷을 통해 외부 서버를 호출하지만,
Ollama는 내 PC의 Docker 컨테이너 안에서 실행되는 로컬 서버입니다.
"""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

# Ollama 컨테이너는 기본적으로 11434 포트에서 REST API를 제공합니다.
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

print(f"Ollama API 주소: {base_url}")

try:
    # /api/tags는 현재 Ollama에 다운로드된 모델 목록을 반환합니다.
    response = httpx.get(f"{base_url}/api/tags", timeout=5.0)

    # HTTP 상태 코드가 400 또는 500번대이면 예외를 발생시킵니다.
    response.raise_for_status()
except httpx.HTTPError as exc:
    print("Ollama 서버에 연결하지 못했습니다.")
    print("확인 순서:")
    print("1. Docker Desktop이 실행 중인지 확인합니다.")
    print("2. docker ps 명령으로 ollama-llm 컨테이너가 실행 중인지 확인합니다.")
    print("3. docker start ollama-llm 명령으로 컨테이너를 다시 시작해 봅니다.")
    print(f"오류 내용: {exc}")
else:
    data = response.json()
    print("Ollama 서버가 실행 중입니다.")
    print("현재 다운로드된 모델 목록 원본 JSON:")
    print(data)
