"""기존 귀가도우미 MCP 연결 설정을 Backend에서 재사용합니다."""

from typing import Any

from mcp import ClientSession

from _stdio_client import MCP_SERVERS, connect_to_mcp_servers


# Backend Agent가 기대하는 이름으로 기존 다중 MCP context manager를 제공합니다.
mcp_sessions = connect_to_mcp_servers


def result_text(result) -> str:
    return "\n".join(
        content.text for content in result.content if hasattr(content, "text")
    )


async def discover_tools() -> list[dict[str, Any]]:
    async with mcp_sessions() as sessions:
        tools: list[dict[str, Any]] = []
        for server_name, session in sessions.items():
            response = await session.list_tools()
            for tool in response.tools:
                raw = tool.model_dump(by_alias=True)
                tools.append({
                    "server": server_name,
                    "name": tool.name,
                    "public_name": f"{server_name}__{tool.name}",
                    "description": tool.description,
                    "input_schema": raw.get("inputSchema", {}),
                })
        return tools


async def discover_resources() -> list[dict[str, Any]]:
    async with mcp_sessions() as sessions:
        resources: list[dict[str, Any]] = []
        for server_name, session in sessions.items():
            response = await session.list_resources()
            resources.extend(
                {
                    "server": server_name,
                    "name": resource.name,
                    "uri": str(resource.uri),
                    "description": resource.description,
                }
                for resource in response.resources
            )
        return resources


async def read_resource(server_name: str, uri: str) -> str:
    async with mcp_sessions() as sessions:
        session: ClientSession = sessions[server_name]
        response = await session.read_resource(uri)
        return "\n".join(
            content.text for content in response.contents if hasattr(content, "text")
        )
