"""날씨 Tool 두 개를 제공하는 Streamable HTTP MCP Server입니다."""

import os

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from weather import get_current_weather as fetch_current_weather


load_dotenv()

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.getenv("MCP_PORT", "8010"))

mcp = FastMCP(
    "weather-mcp",
    instructions="기상청 날씨 정보를 제공하는 학습용 MCP Server입니다.",
    host=MCP_HOST,
    port=MCP_PORT,
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def get_current_weather(location: str) -> dict:
    """지역의 현재 날씨를 조회합니다."""
    return fetch_current_weather(location)


@mcp.tool()
def get_next_week_weather(location: str) -> dict:
    """지역의 4일 후부터 10일 후까지 중기예보를 조회합니다."""
    return {
        "location": location,
        "message": "다음 주 날씨 Tool 연결에 성공했습니다.",
        "status": "temporary",
    }


if __name__ == "__main__":
    try:
        mcp.run(transport="streamable-http")
    except KeyboardInterrupt:
        pass
