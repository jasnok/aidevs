r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\99_final-agent-project\team-template\frontend

실행 명령:
    streamlit run .\app.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""팀 프로젝트 Streamlit 시작 화면입니다."""

from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from graph import run_agent  # noqa: E402


st.set_page_config(page_title="Team Agent", layout="wide")
st.title("Team Agent Project")

user_request = st.text_area("요청", value="수업 자료를 검색해줘", height=120)

if st.button("실행"):
    result = run_agent(user_request)
    st.subheader("최종 답변")
    st.write(result["final_answer"])
    st.subheader("State")
    st.json(result)
