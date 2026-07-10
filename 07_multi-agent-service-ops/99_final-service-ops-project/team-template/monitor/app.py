r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\team-template\monitor

Run command:
    streamlit run .\app.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Auto Healing 운영 모니터 화면입니다."""

import httpx
import streamlit as st


st.set_page_config(page_title="Auto Healing Monitor", layout="wide")
st.title("Auto Healing Monitor")

try:
    health = httpx.get("http://backend:8000/health", timeout=5).json()
    st.success("backend health check 성공")
    st.json(health)
except httpx.HTTPError as exc:
    st.error(f"backend health check 실패: {exc}")

st.subheader("Event History")
try:
    events = httpx.get("http://backend:8000/events", timeout=5).json()
    st.dataframe(events, use_container_width=True)
except httpx.HTTPError as exc:
    st.error(f"event 조회 실패: {exc}")
