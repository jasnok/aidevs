r"""MCP 서버의 course_search Tool을 호출하는 클라이언트 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use

실행 명령:
    python .\05_mcp-concept-and-optional-practice\03_mcp_client_test.py

필요한 준비:
    pip install mcp

이 파일은 02_simple_mcp_server.py를 stdio 방식으로 실행한 뒤,
서버가 제공하는 Tool 목록을 확인하고 course_search Tool을 호출합니다.
"""

from pathlib import Path
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_FILE = Path(__file__).resolve().parent / "02_simple_mcp_server.py"


async def main() -> None:
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_FILE)],
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("MCP 서버가 제공하는 Tool 목록:")
            for item in tools.tools:
                print("-", item.name, ":", item.description)

            result = await session.call_tool("course_search", {"query": "LangGraph"})
            print("\ncourse_search 결과:")
            for content in result.content:
                print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
