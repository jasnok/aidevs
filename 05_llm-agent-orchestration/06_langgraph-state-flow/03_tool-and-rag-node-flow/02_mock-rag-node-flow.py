r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\03_tool-and-rag-node-flow

실행 명령:
    python .\02_mock-rag-node-flow.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Mock 문서 검색 노드를 포함한 RAG 흐름 예제입니다."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


DOCUMENTS = [
    "FastAPI는 Python으로 API 서버를 만드는 웹 프레임워크입니다.",
    "Streamlit은 Python으로 데이터 앱과 대시보드를 빠르게 만들 수 있습니다.",
    "LangGraph는 상태 기반 에이전트 흐름을 그래프로 구성하는 도구입니다.",
]


class RagFlowState(TypedDict):
    """RAG 흐름에서 사용할 상태입니다."""

    question: str
    retrieved_context: list[str]
    answer: str


def retrieve_context(state: RagFlowState) -> dict:
    """질문에 포함된 키워드로 관련 문서를 단순 검색합니다."""
    question = state["question"]
    contexts = [doc for doc in DOCUMENTS if any(word in doc for word in question.split())]
    if not contexts:
        contexts = ["관련 문서를 찾지 못했습니다."]
    return {"retrieved_context": contexts}


def generate_answer(state: RagFlowState) -> dict:
    """검색된 context를 바탕으로 답변을 생성합니다."""
    context_text = " ".join(state["retrieved_context"])
    return {"answer": f"검색 근거: {context_text}"}


graph_builder = StateGraph(RagFlowState)
graph_builder.add_node("retrieve_context", retrieve_context)
graph_builder.add_node("generate_answer", generate_answer)

graph_builder.add_edge(START, "retrieve_context")
graph_builder.add_edge("retrieve_context", "generate_answer")
graph_builder.add_edge("generate_answer", END)

graph = graph_builder.compile()

result = graph.invoke({"question": "LangGraph는 무엇인가요?", "retrieved_context": [], "answer": ""})
print(result["answer"])
