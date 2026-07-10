r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\01_function-calling-basic

실행 명령:
    python .\01_simple-calculator-tool.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""OpenAI Function Calling으로 간단한 계산 도구를 호출하는 예제입니다."""

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


def add_numbers(a: int, b: int) -> int:
    """두 정수를 더합니다."""
    return a + b


def call_function(name: str, arguments: dict) -> str:
    """모델이 요청한 함수 이름을 실제 Python 함수에 연결합니다."""
    if name == "add_numbers":
        result = add_numbers(arguments["a"], arguments["b"])
        return json.dumps({"result": result}, ensure_ascii=False)
    return json.dumps({"error": f"Unknown function: {name}"}, ensure_ascii=False)


client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "add_numbers",
        "description": "Add two integer numbers and return the result.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer", "description": "First number"},
                "b": {"type": "integer", "description": "Second number"},
            },
            "required": ["a", "b"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

input_messages = [
    {
        "role": "user",
        "content": "17과 25를 더한 값을 계산하고, 결과를 한 문장으로 알려줘.",
    }
]

# 첫 번째 요청에서는 모델에게 사용할 수 있는 도구 목록을 전달합니다.
response = client.responses.create(model=model, input=input_messages, tools=tools)

# reasoning 모델은 tool call과 함께 반환된 output 항목을 다음 요청에 함께 넘기는 것이 안전합니다.
input_messages += response.output

for item in response.output:
    if item.type != "function_call":
        continue

    # 모델이 만든 JSON 문자열 인자를 Python dict로 바꿉니다.
    arguments = json.loads(item.arguments)
    tool_result = call_function(item.name, arguments)

    # 함수 실행 결과를 function_call_output으로 모델에게 다시 전달합니다.
    input_messages.append(
        {
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": tool_result,
        }
    )

# 두 번째 요청에서는 도구 실행 결과를 포함해 최종 답변을 요청합니다.
final_response = client.responses.create(model=model, input=input_messages, tools=tools)
print(final_response.output_text)
