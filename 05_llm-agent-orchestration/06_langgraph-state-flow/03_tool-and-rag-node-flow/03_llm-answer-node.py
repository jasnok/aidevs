r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\06_langgraph-state-flow\03_tool-and-rag-node-flow

실행 명령:
    python .\03_llm-answer-node.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""LangGraph 노드 안에서 OpenAI 모델을 호출해 답변을 생성하는 예제입니다."""

from pathlib import Path
import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 LLM 노드 예제를 건너뜁니다.")
    raise SystemExit(0)


class LlmState(TypedDict):
    """LLM 답변 노드에서 사용할 상태입니다."""

    question: str
    context: str
    answer: str


def generate_llm_answer(state: LlmState) -> dict:
    """상태의 question과 context를 사용해 LLM 답변을 생성합니다."""
    model = ChatOpenAI(model=model_name)
    prompt = f"""
    너는 수업 안내 도우미다.
    아래 context를 근거로 질문에 답하라.

    context:
    {state['context']}

    question:
    {state['question']}
    """.strip()
    response = model.invoke(prompt)
    return {"answer": response.content}


graph_builder = StateGraph(LlmState)
graph_builder.add_node("generate_llm_answer", generate_llm_answer)
graph_builder.add_edge(START, "generate_llm_answer")
graph_builder.add_edge("generate_llm_answer", END)

graph = graph_builder.compile()

result = graph.invoke(
    {
        "question": "LangGraph는 언제 사용하면 좋나요?",
        "context": "LangGraph는 상태 기반 에이전트 흐름을 그래프로 구성하는 도구입니다.",
        "answer": "",
    }
)

print(result["answer"])
