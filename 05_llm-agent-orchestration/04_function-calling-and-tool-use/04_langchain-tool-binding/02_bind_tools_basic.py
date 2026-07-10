r"""ChatOpenAI에 Tool을 바인딩하는 최소 예제입니다.

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use

실행 명령:
    python .\04_langchain-tool-binding\02_bind_tools_basic.py

필요한 준비:
    1. .env 파일에 OPENAI_API_KEY가 있어야 합니다.
    2. pip install langchain-openai langchain-core python-dotenv

중요:
    모델은 "어떤 Tool을 쓰면 좋겠다"고 제안할 수 있습니다.
    실제 Tool 실행은 Python 코드가 담당합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


@tool
def get_learning_log_summary(topic: str) -> str:
    """주제별 학습 로그 요약을 반환합니다."""
    logs = {
        "fastapi": "FastAPI는 라우팅, Pydantic 검증, 예외 처리를 중심으로 복습하세요.",
        "rag": "RAG는 문서 chunking, embedding, pgvector 검색, 답변 근거 확인을 연결해서 보세요.",
        "langgraph": "LangGraph는 State, Node, Edge, 조건 분기 흐름을 함께 봐야 합니다.",
    }
    return logs.get(topic.lower(), "해당 주제의 학습 로그가 아직 없습니다.")


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key or api_key == "your-openai-api-key":
        print("OPENAI_API_KEY가 설정되지 않아 모델 호출을 건너뜁니다.")
        print("Tool binding 구조만 확인하려면 01_langchain_tool_decorator.py를 먼저 실행하세요.")
        return

    model = ChatOpenAI(model=model_name)
    model_with_tools = model.bind_tools([get_learning_log_summary])

    response = model_with_tools.invoke("RAG를 복습하려면 무엇을 보면 좋을까?")

    print("모델 응답:")
    print(response)
    print("\n모델이 제안한 tool_calls:")
    print(response.tool_calls)

    if response.tool_calls:
        first_call = response.tool_calls[0]
        tool_result = get_learning_log_summary.invoke(first_call["args"])
        print("\nPython 코드가 실제 Tool을 실행한 결과:")
        print(tool_result)


if __name__ == "__main__":
    main()
