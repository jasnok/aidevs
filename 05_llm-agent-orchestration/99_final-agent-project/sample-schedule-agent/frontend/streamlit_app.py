r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\sample-schedule-agent\frontend

실행 명령:
    streamlit run .\streamlit_app.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""일정 조정 에이전트를 실행하는 Streamlit 화면입니다."""

from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.graph import run_agent  # noqa: E402


st.set_page_config(page_title="Schedule Agent", layout="wide")
st.title("일정 조정 에이전트")

user_request = st.text_area(
    "요청",
    value="Kim, Lee, Park 세 명이 가능한 30분 회의 시간을 찾아줘.",
    height=120,
)
duration_minutes = st.number_input("회의 시간(분)", min_value=10, max_value=180, value=30, step=10)

if st.button("에이전트 실행"):
    with st.spinner("일정을 분석하는 중입니다..."):
        result = run_agent(user_request, duration_minutes)

    st.subheader("최종 답변")
    st.write(result["final_answer"])

    st.subheader("상태 확인")
    st.json(result)
