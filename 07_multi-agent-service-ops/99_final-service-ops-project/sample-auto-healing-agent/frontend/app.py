r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\99_final-service-ops-project\sample-auto-healing-agent\frontend

Run command:
    streamlit run .\app.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Auto Healing Agent 사용자 화면입니다."""

import httpx
import streamlit as st


st.set_page_config(page_title="Auto Healing Agent", layout="wide")
st.title("Auto Healing Agent")

service_name = st.text_input("서비스 이름", value="backend")
failure_message = st.text_area("장애 메시지", value="backend health check failed", height=120)

if st.button("Auto Healing 실행"):
    try:
        response = httpx.post(
            "http://backend:8000/heal",
            json={"service_name": service_name, "failure_message": failure_message},
            timeout=5,
        )
        response.raise_for_status()
        st.success("Auto Healing 분석 완료")
        st.json(response.json())
    except httpx.HTTPError as exc:
        st.error(f"backend 연결 실패: {exc}")
