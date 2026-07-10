r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\01_llm-api-and-local-llm\02_ollama-docker-llama

실행 명령:
    python .\02_ollama-generate.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Ollama REST API로 로컬 Llama 모델을 호출하는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
model = os.getenv("OLLAMA_MODEL", "llama3.2")

# Ollama의 /api/generate 엔드포인트에 보낼 요청 데이터입니다.
# stream=False로 설정하면 응답을 조각 단위로 받지 않고 한 번에 받습니다.
prompt = "Python을 처음 배우는 사람에게 함수가 무엇인지 두 문장으로 설명해줘."
payload = {
    "model": model,
    "prompt": prompt,
    "stream": False,
}

print(f"Ollama API 주소: {base_url}")
print(f"사용 모델: {model}")
print("[요청]")
print(prompt)

try:
    response = httpx.post(f"{base_url}/api/generate", json=payload, timeout=120.0)
    response.raise_for_status()
except httpx.HTTPError as exc:
    print("Llama 모델 호출에 실패했습니다.")
    print("확인 순서:")
    print("1. docker ps로 ollama-llm 컨테이너 실행 여부를 확인합니다.")
    print("2. docker exec -it ollama-llm ollama list로 llama3.2 모델이 있는지 확인합니다.")
    print("3. 모델이 없다면 docker exec -it ollama-llm ollama pull llama3.2를 실행합니다.")
    print(f"오류 내용: {exc}")
else:
    data = response.json()
    print("\n[원본 응답 JSON]")
    print(data)
    print("\n[응답 텍스트]")
    print(data.get("response", "응답 텍스트를 찾지 못했습니다."))
