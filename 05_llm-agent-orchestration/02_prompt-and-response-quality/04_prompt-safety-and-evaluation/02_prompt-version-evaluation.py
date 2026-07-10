r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\02_prompt-and-response-quality\04_prompt-safety-and-evaluation

실행 명령:
    python .\02_prompt-version-evaluation.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""프롬프트 버전별 응답을 비교하는 간단한 평가 예제입니다."""

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

test_question = "Docker run으로 Ollama 컨테이너를 실행하는 과정을 초보자에게 설명해줘."

# 같은 질문에 대해 프롬프트 지시문만 바꾸어 응답 품질을 비교합니다.
prompts = {
    "v1": "질문에 답해줘.",
    "v2": "초보자를 대상으로 쉬운 비유와 함께 5문장 이내로 답해줘.",
    "v3": "초보자를 대상으로 답하되, 표와 예시 명령어를 포함하고 과장 없이 설명해줘.",
}

print(f"사용 모델: {model}")
print("[테스트 질문]")
print(test_question)

for version, instruction in prompts.items():
    print(f"\n===== {version} =====")
    print("[지시문]")
    print(instruction)

    response = client.responses.create(
        model=model,
        input=f"{instruction}\n\n질문: {test_question}",
    )

    print("\n[응답]")
    print(response.output_text)

print("\n[평가 기준]")
print("- 쉬운가?")
print("- 정확한가?")
print("- 출력 형식을 잘 지키는가?")
print("- 수업이나 프로젝트 문서에 바로 활용할 수 있는가?")
