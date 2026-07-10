r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\01_function-calling-basic

실행 명령:
    python .\02_learning-log-summary-tool.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""학습 로그 데이터를 조회하는 도구를 Function Calling으로 연결하는 예제입니다."""

from pathlib import Path
import json
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

LEARNING_LOGS = [
    {"learner": "Kim", "topic": "FastAPI", "minutes": 80, "status": "done"},
    {"learner": "Kim", "topic": "Streamlit", "minutes": 40, "status": "doing"},
    {"learner": "Lee", "topic": "Docker", "minutes": 60, "status": "done"},
]


def get_learning_logs(learner: str) -> list[dict]:
    """학습자 이름으로 학습 로그를 조회합니다."""
    return [log for log in LEARNING_LOGS if log["learner"].lower() == learner.lower()]


def call_function(name: str, arguments: dict) -> str:
    """도구 이름을 실제 Python 함수에 연결합니다."""
    if name == "get_learning_logs":
        logs = get_learning_logs(arguments["learner"])
        return json.dumps({"logs": logs}, ensure_ascii=False)
    return json.dumps({"error": f"Unknown function: {name}"}, ensure_ascii=False)


client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_learning_logs",
        "description": "Get learning logs for a learner by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "learner": {"type": "string", "description": "Learner name"},
            },
            "required": ["learner"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

input_messages = [
    {
        "role": "user",
        "content": "Kim 학습자의 학습 로그를 조회해서 총 학습 시간과 진행 중인 주제를 알려줘.",
    }
]

response = client.responses.create(model=model, input=input_messages, tools=tools)
input_messages += response.output

for item in response.output:
    if item.type != "function_call":
        continue

    arguments = json.loads(item.arguments)
    tool_result = call_function(item.name, arguments)
    input_messages.append(
        {
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": tool_result,
        }
    )

final_response = client.responses.create(model=model, input=input_messages, tools=tools)
print(final_response.output_text)
