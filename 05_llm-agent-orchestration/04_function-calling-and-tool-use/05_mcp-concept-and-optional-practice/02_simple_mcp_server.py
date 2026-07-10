r"""아주 작은 MCP 서버 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use

직접 서버 실행:
    python .\05_mcp-concept-and-optional-practice\02_simple_mcp_server.py

클라이언트 테스트:
    python .\05_mcp-concept-and-optional-practice\03_mcp_client_test.py

필요한 준비:
    pip install mcp

이 예제는 선택 심화입니다.
05 과정의 필수 목표는 MCP 서버를 깊게 구현하는 것이 아니라,
외부 도구를 표준 방식으로 제공할 수 있다는 감각을 잡는 것입니다.
"""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("aidev-course-tools")

COURSE_NOTES = {
    "prompt": "Prompt는 Role, Instruction, Context, Output Format을 나누어 설계합니다.",
    "tool": "Tool은 LLM이 직접 실행하는 것이 아니라 Python 코드가 실행하는 외부 기능입니다.",
    "rag": "RAG는 문서를 검색해 context로 넣고, 그 근거로 답변하게 만드는 구조입니다.",
    "langgraph": "LangGraph는 State, Node, Edge로 Agent 실행 흐름을 관리합니다.",
}


@mcp.tool()
def course_search(query: str) -> str:
    """05 과정 노트에서 query와 관련 있는 설명을 검색합니다."""
    lowered = query.lower()
    for keyword, note in COURSE_NOTES.items():
        if keyword in lowered:
            return note
    return "관련 노트를 찾지 못했습니다. prompt, tool, rag, langgraph 중 하나로 검색해 보세요."


if __name__ == "__main__":
    mcp.run()
