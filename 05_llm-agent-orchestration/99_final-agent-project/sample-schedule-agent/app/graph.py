r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent\app

실행 명령:
    python .\graph.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""LangGraph로 구성한 일정 조정 에이전트 샘플입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

from app.schemas import AgentState
from app.tools import (
    build_rule_based_message,
    extract_participants,
    find_common_available_slots,
    select_best_slot,
)


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


def analyze_request(state: AgentState) -> dict:
    """사용자 요청에서 참석자와 회의 시간을 추출합니다."""
    participants = extract_participants(state["user_request"])
    return {"participants": participants, "duration_minutes": state.get("duration_minutes", 30) or 30}


def check_schedules(state: AgentState) -> dict:
    """참석자들의 공통 가능 시간대를 찾습니다."""
    slots = find_common_available_slots(state["participants"])
    return {"available_slots": slots}


def choose_slot(state: AgentState) -> dict:
    """가능한 시간대 중 하나를 선택합니다."""
    return {"selected_slot": select_best_slot(state["available_slots"])}


def draft_message(state: AgentState) -> dict:
    """OpenAI API Key가 있으면 LLM으로, 없으면 규칙 기반으로 제안 메시지를 만듭니다."""
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key or api_key == "your-openai-api-key":
        message = build_rule_based_message(
            state["participants"],
            state["selected_slot"],
            state["duration_minutes"],
        )
        return {"draft_message": message}

    model = ChatOpenAI(model=model_name)
    prompt = f"""
    너는 일정 조정 비서다.
    아래 정보를 바탕으로 정중하고 짧은 일정 제안 메시지를 작성하라.

    참석자: {', '.join(state['participants'])}
    선택 시간: {state['selected_slot'] or '공통 가능 시간 없음'}
    회의 시간: {state['duration_minutes']}분
    사용자 요청: {state['user_request']}
    """.strip()
    response = model.invoke(prompt)
    return {"draft_message": response.content}


def finalize_answer(state: AgentState) -> dict:
    """최종 사용자 응답을 구성합니다."""
    if not state["selected_slot"]:
        return {"final_answer": state["draft_message"]}

    slots = ", ".join(state["available_slots"])
    final = f"가능한 후보: {slots}\n\n제안 메시지:\n{state['draft_message']}"
    return {"final_answer": final}


def build_graph():
    """일정 조정 에이전트 그래프를 생성합니다."""
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("analyze_request", analyze_request)
    graph_builder.add_node("check_schedules", check_schedules)
    graph_builder.add_node("choose_slot", choose_slot)
    graph_builder.add_node("draft_message", draft_message)
    graph_builder.add_node("finalize_answer", finalize_answer)

    graph_builder.add_edge(START, "analyze_request")
    graph_builder.add_edge("analyze_request", "check_schedules")
    graph_builder.add_edge("check_schedules", "choose_slot")
    graph_builder.add_edge("choose_slot", "draft_message")
    graph_builder.add_edge("draft_message", "finalize_answer")
    graph_builder.add_edge("finalize_answer", END)

    return graph_builder.compile()


def run_agent(user_request: str, duration_minutes: int = 30) -> AgentState:
    """사용자 요청을 받아 에이전트 그래프를 실행합니다."""
    graph = build_graph()
    initial_state: AgentState = {
        "user_request": user_request,
        "participants": [],
        "duration_minutes": duration_minutes,
        "available_slots": [],
        "selected_slot": "",
        "draft_message": "",
        "final_answer": "",
    }
    return graph.invoke(initial_state)


if __name__ == "__main__":
    result = run_agent("Kim, Lee, Park 세 명이 가능한 30분 회의 시간을 찾아줘.")
    print(result["final_answer"])
