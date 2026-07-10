r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\03_tool-and-rag-node-flow

실행 명령:
    python .\04_hybrid-memory-flow.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""Session Memory와 Vector Memory를 함께 사용하는 LangGraph 예제입니다.

Session Memory는 현재 대화의 짧은 기억이고,
Vector Memory는 장기적으로 검색 가능한 지식 저장소라고 볼 수 있습니다.
이 예제는 실제 DB 없이 두 메모리를 mock 데이터로 표현합니다.
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


SESSION_MESSAGES = [
    "사용자는 FastAPI를 배우는 중입니다.",
    "사용자는 Docker Compose는 07 과정에서 배우기로 했습니다.",
]

VECTOR_MEMORY = [
    "05 과정에서는 docker run으로 Ollama와 pgvector를 실행합니다.",
    "LangGraph는 Node, Edge, State로 에이전트 흐름을 구성합니다.",
    "RAG는 검색 결과를 context로 넣어 답변 품질을 높이는 구조입니다.",
]


class HybridMemoryState(TypedDict):
    """Hybrid Memory 그래프에서 공유할 상태입니다."""

    question: str
    session_context: list[str]
    vector_context: list[str]
    answer: str


def load_session_memory(state: HybridMemoryState) -> dict:
    """현재 사용자 세션의 최근 대화 기억을 불러옵니다."""

    return {"session_context": SESSION_MESSAGES[-2:]}


def retrieve_vector_memory(state: HybridMemoryState) -> dict:
    """질문과 관련 있는 장기 기억을 간단한 키워드 방식으로 찾습니다."""

    question = state["question"]
    matches = [item for item in VECTOR_MEMORY if any(word in item for word in question.split())]
    if not matches:
        matches = ["관련 장기 기억을 찾지 못했습니다."]
    return {"vector_context": matches}


def generate_answer(state: HybridMemoryState) -> dict:
    """Session Memory와 Vector Memory를 함께 사용해 답변을 만듭니다."""

    session_text = " / ".join(state["session_context"])
    vector_text = " / ".join(state["vector_context"])
    answer = (
        f"질문: {state['question']}\n"
        f"세션 기억: {session_text}\n"
        f"장기 기억: {vector_text}\n"
        "답변: 현재 과정에서는 필요한 기억을 나누어 불러온 뒤 함께 context로 구성합니다."
    )
    return {"answer": answer}


graph_builder = StateGraph(HybridMemoryState)
graph_builder.add_node("load_session_memory", load_session_memory)
graph_builder.add_node("retrieve_vector_memory", retrieve_vector_memory)
graph_builder.add_node("generate_answer", generate_answer)

graph_builder.add_edge(START, "load_session_memory")
graph_builder.add_edge("load_session_memory", "retrieve_vector_memory")
graph_builder.add_edge("retrieve_vector_memory", "generate_answer")
graph_builder.add_edge("generate_answer", END)

graph = graph_builder.compile()

result = graph.invoke(
    {
        "question": "LangGraph와 RAG는 어떻게 연결되나요?",
        "session_context": [],
        "vector_context": [],
        "answer": "",
    }
)

print(result["answer"])
