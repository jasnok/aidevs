r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\03_openai-vs-llama-comparison

실행 명령:
    python .\02_compare-prompt-style.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""출력 형식을 지정했을 때 OpenAI와 Llama 응답을 비교하는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

# 이번 프롬프트는 답변 형식을 일부러 고정합니다.
# 이 실습의 목적은 두 모델이 출력 형식을 얼마나 잘 지키는지 비교하는 것입니다.
PROMPT = """
Python 리스트를 초보자에게 설명해줘.
반드시 아래 형식으로만 답변해줘.

개념: 한 문장
예시: 짧은 코드 한 줄
주의점: 한 문장
""".strip()


def call_openai(prompt: str) -> str:
    """OpenAI API에 형식 고정 프롬프트를 보냅니다."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-openai-api-key":
        return "OPENAI_API_KEY가 설정되지 않아 호출하지 않았습니다."

    client = OpenAI()
    response = client.responses.create(model=OPENAI_MODEL, input=prompt)
    return response.output_text


def call_ollama(prompt: str) -> str:
    """Ollama API에 형식 고정 프롬프트를 보냅니다."""

    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}

    try:
        response = httpx.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=120.0)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        return f"Ollama 호출에 실패했습니다: {exc}"

    data = response.json()
    return data.get("response", "응답 텍스트를 찾지 못했습니다.")


print("[프롬프트]")
print(PROMPT)

print("\n[OpenAI 응답]")
print(f"모델: {OPENAI_MODEL}")
print(call_openai(PROMPT))

print("\n[Llama 응답]")
print(f"모델: {OLLAMA_MODEL}")
print(call_ollama(PROMPT))

print("\n[확인할 점]")
print("- 개념/예시/주의점 형식을 지켰는가?")
print("- 설명이 초보자가 이해하기 쉬운가?")
print("- 불필요한 문장이 추가되었는가?")
