"""로컬 및 원격 MCP Server를 함께 연결하는 Client 도우미입니다."""

import os
import sys
from contextlib import AsyncExitStack, asynccontextmanager
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")
SERVER_PATH = Path(__file__).with_name("mcp_server.py")

# 팀원 접속 정보는 프로젝트 루트의 .env에서 가져옵니다.
def required_env(name: str) -> str:
    """필수 환경변수를 읽고 없으면 실제 값을 노출하지 않는 오류를 발생시킵니다."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"필수 환경변수 {name}을(를) .env에 설정하세요.")
    return value


def required_port(name: str) -> int:
    """필수 포트 환경변수를 읽고 유효한 범위인지 검사합니다."""
    raw = required_env(name)
    try:
        port = int(raw)
    except ValueError as exc:
        raise RuntimeError(f"환경변수 {name}은 숫자여야 합니다.") from exc
    if not 1 <= port <= 65_535:
        raise RuntimeError(f"환경변수 {name}은 1~65535 범위여야 합니다.")
    return port


ALCOHOL_MCP_IP = required_env("ALCOHOL_MCP_IP")
ALCOHOL_MCP_PORT = required_port("ALCOHOL_MCP_PORT")
FOOD_MCP_IP = required_env("FOOD_MCP_IP")
FOOD_MCP_PORT = required_port("FOOD_MCP_PORT")


MCP_SERVERS: dict[str, dict[str, Any]] = {
    "return_home": {
        "transport": "stdio",
        "command": sys.executable,
        "args": [str(SERVER_PATH)],
    },
    "alcohol": {
        "transport": "streamable-http",
        "url": f"http://{ALCOHOL_MCP_IP}:{ALCOHOL_MCP_PORT}/mcp",
    },
    "food": {
        "transport": "streamable-http",
        "url": f"http://{FOOD_MCP_IP}:{FOOD_MCP_PORT}/mcp",
    },
}


async def open_session(
    stack: AsyncExitStack,
    config: dict[str, Any],
) -> ClientSession:
    """설정에 맞는 Transport를 열고 초기화된 MCP Session을 반환합니다."""
    transport = config["transport"]

    if transport == "streamable-http":
        read_stream, write_stream, _ = await stack.enter_async_context(
            streamable_http_client(config["url"])
        )
    elif transport == "stdio":
        parameters = StdioServerParameters(
            command=config["command"],
            args=config.get("args", []),
            env=config.get("env"),
        )
        read_stream, write_stream = await stack.enter_async_context(
            stdio_client(parameters)
        )
    else:
        raise ValueError(f"지원하지 않는 MCP Transport입니다: {transport}")

    session = await stack.enter_async_context(
        ClientSession(read_stream, write_stream)
    )
    await session.initialize()
    return session


@asynccontextmanager
async def connect_to_mcp_servers():
    """귀가, 주류, 음식 MCP Server를 연결하고 이름별 Session을 제공합니다."""
    async with AsyncExitStack() as stack:
        sessions: dict[str, ClientSession] = {}
        for server_name, config in MCP_SERVERS.items():
            sessions[server_name] = await open_session(stack, config)
        yield sessions
