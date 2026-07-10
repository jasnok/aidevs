r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\team-template\backend

실행 명령:
    python .\agent_state.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""팀 프로젝트의 AgentState를 정의하는 파일입니다."""

from typing import TypedDict


class AgentState(TypedDict):
    """팀 주제에 맞게 필드를 수정하세요."""

    user_request: str
    route: str
    tool_result: str
    retrieved_context: list[str]
    final_answer: str
