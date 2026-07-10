r"""RUN GUIDE

Run from:
    C:\aidev\07_multi-agent-service-ops\05_observability-and-ops-dashboard\03_ops-dashboard-streamlit

Run command:
    streamlit run .\01_ops-dashboard.py

Purpose:
    Small example file for the 07 service-ops course.
"""

"""Streamlit 기반 운영 대시보드 예제입니다."""

from datetime import datetime

import streamlit as st


SERVICES = [
    {"service": "backend", "status": "healthy", "port": 8000, "last_check": "방금 전"},
    {"service": "worker", "status": "running", "port": None, "last_check": "1분 전"},
    {"service": "monitor", "status": "healthy", "port": 8802, "last_check": "방금 전"},
]

EVENTS = [
    {"time": "10:00", "agent": "supervisor_agent", "event": "request_received", "status": "success"},
    {"time": "10:01", "agent": "ops_agent", "event": "health_check", "status": "success"},
    {"time": "10:02", "agent": "reviewer_agent", "event": "quality_check", "status": "success"},
]


st.set_page_config(page_title="Ops Dashboard", layout="wide")
st.title("Ops Dashboard")
st.caption(f"last refresh: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

healthy_count = sum(1 for service in SERVICES if service["status"] == "healthy")
running_count = sum(1 for service in SERVICES if service["status"] == "running")
failed_count = sum(1 for event in EVENTS if event["status"] == "failed")

col1, col2, col3 = st.columns(3)
col1.metric("Healthy Services", healthy_count)
col2.metric("Running Workers", running_count)
col3.metric("Failed Events", failed_count)

st.subheader("Service Status")
st.dataframe(SERVICES, use_container_width=True)

st.subheader("Recent Events")
st.dataframe(EVENTS, use_container_width=True)

st.subheader("운영 메모")
st.write("실제 프로젝트에서는 이 화면이 Docker Compose monitor 서비스 또는 AWS 운영 대시보드와 연결됩니다.")
