# ai_agent.py

"""GPT가 MCP Tool을 선택해 안전한 귀가 방법을 안내하는 예제입니다.

실행 전 준비
    1. 과정 루트의 ``.env``에 ``OPENAI_API_KEY``와 ``OPENAI_MODEL``을 설정합니다.
    2. 가상환경에서 ``pip install -r requirements.txt``를 실행합니다.
    3. 이 파일만 실행합니다. ``mcp_server.py``는 직접 실행하지 않습니다.

실행 명령
    cd C:\\aidevs\\05_llm-agent-orchestration\\03_mcp\\0826_lab
    python .\\ai_agent.py

전체 흐름
    사용자 질문
    → stdio MCP Client가 ``mcp_server.py``를 자식 프로세스로 자동 실행
    → MCP ``initialize``로 Client와 Server 기능 협상
    → MCP ``tools/list``로 귀가 교통 Tool과 arguments Schema 발견
    → MCP Schema를 OpenAI Responses API의 Function Tool Schema로 변환
    → GPT가 질문과 Schema를 보고 필요한 Tool 이름과 arguments 제안
    → Client가 제안된 이름을 MCP Tool allowlist와 비교
    → MCP ``tools/call``로 Server에 실행 요청
    → Server가 arguments를 검증하고 Python Tool 실행
    → 모든 Tool Result를 ``function_call_output``과 ``call_id``로 GPT에 전달
    → 두 번째 GPT 호출은 Tool 없이 결과를 종합한 한국어 최종 답변 반환
    → Client 종료 시 stdio MCP Server 자식 프로세스도 종료

역할과 권한 경계
    - GPT: 어떤 Tool이 필요한지와 arguments를 제안합니다.
    - MCP Client: Tool 발견, allowlist 검사, 호출, 결과 전달을 담당합니다.
    - MCP Server: arguments 검증과 실제 Python 함수 실행을 담당합니다.
    - GPT는 Python 함수를 직접 실행하지 않으며 Server의 실행 권한도 갖지 않습니다.

종료 조건과 안전장치
    - 첫 GPT 응답에 Function Call이 없으면 해당 응답으로 바로 종료합니다.
    - Server가 공개하지 않은 Tool 이름은 실행하지 않습니다.
    - arguments는 JSON Object인지 확인한 뒤 Server에서 다시 검증합니다.
    - 모든 Tool Call, arguments, 결과, 오류 여부를 ``trace``에 기록합니다.

이 예제에서 Loop를 사용하지 않는 이유
    귀가에 필요한 네 가지 교통수단을 하나의 Tool이 함께 반환하므로, Tool 실행 뒤
    두 번째 GPT 호출에서 결과를 비교해 최종 답변을 만들면 충분합니다.
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import AsyncOpenAI

from _stdio_client import connect_to_return_home_server


ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
INSTRUCTIONS = (
    "당신은 술집 이용 후 안전한 귀가를 돕는 Agent입니다. "
    "목적지가 있는 귀가 질문에는 get_return_transport_options를 호출하세요. "
    "목적지가 없으면 추측하지 말고 물어보세요. Tool 결과의 지하철, 버스, 택시, "
    "대리기사를 시간과 비용 기준으로 비교해 한국어로 간단히 추천하세요. "
    "대리기사는 사용자의 차량이 있을 때만 추천하고, Tool에 없는 정보는 만들지 마세요. "
    "Mock 교통 정보는 실제 출발 전에 확인해야 한다고 알리세요."
)


def to_openai_tool(tool) -> dict[str, Any]:
    """MCP Tool Schema를 OpenAI Responses API의 Function Tool로 변환합니다."""
    raw = tool.model_dump(by_alias=True)
    return {
        "type": "function",
        "name": tool.name,
        "description": tool.description or "",
        "parameters": raw["inputSchema"],
        "strict": False,
    }


def text_result(result) -> str:
    return "\n".join(
        content.text for content in result.content if hasattr(content, "text")
    )


async def answer(question: str) -> dict[str, Any]:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY가 필요합니다.")

    trace: list[dict[str, Any]] = []

    async with AsyncOpenAI() as client, connect_to_return_home_server() as session:
        discovered = (await session.list_tools()).tools
        available = {tool.name for tool in discovered}
        openai_tools = [to_openai_tool(tool) for tool in discovered]
        response = await client.responses.create(
            model=OPENAI_MODEL,
            instructions=INSTRUCTIONS,
            input=question,
            tools=openai_tools,
            parallel_tool_calls=True,
        )

        tool_calls = [item for item in response.output if item.type == "function_call"]
        if not tool_calls:
            return {
                "question": question,
                "model": OPENAI_MODEL,
                "discovered_tools": sorted(available),
                "llm_calls": 1,
                "trace": trace,
                "answer": response.output_text,
            }

        tool_outputs = []
        for call in tool_calls:
            if call.name not in available:
                raise ValueError(f"MCP Server가 제공하지 않는 Tool입니다: {call.name}")
            arguments = json.loads(call.arguments)
            if not isinstance(arguments, dict):
                raise ValueError("Tool arguments는 JSON Object여야 합니다.")

            result = await session.call_tool(call.name, arguments)
            result_text = text_result(result)
            trace.append({
                "tool": call.name,
                "arguments": arguments,
                "is_error": bool(result.isError),
                "result": result_text,
            })
            tool_outputs.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": result_text,
            })

        final_response = await client.responses.create(
            model=OPENAI_MODEL,
            instructions=INSTRUCTIONS,
            previous_response_id=response.id,
            input=tool_outputs,
        )
        return {
            "question": question,
            "model": OPENAI_MODEL,
            "discovered_tools": sorted(available),
            "llm_calls": 2,
            "trace": trace,
            "answer": final_response.output_text,
        }


async def main() -> None:
    # result = await answer("서울대입구역까지 어떻게 가?")
    # result = await answer("지금 홍대입구역까지 버스로 갈 수 있어?")
    result = await answer("밤 11시 50분에 강남역까지 어떤 교통수단이 좋아?")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
