"""Streamlit 일정 조정 Agent UI starter입니다.

실행 위치:
    C:\aidev\06_llm-agent-mini-project\team-schedule-agent\frontend

실행 명령:
    streamlit run app.py

구현할 내용:
    1. 사용자 일정 요청을 입력받습니다.
    2. backend의 /agent/schedule API를 호출합니다.
    3. Agent 응답, Tool 호출 이력, 오류 횟수를 화면에 표시합니다.
"""

import streamlit as st


st.set_page_config(page_title="Schedule Agent")
st.title("일정 조정 에이전트")

backend_url = st.text_input("Backend URL", value="http://127.0.0.1:8000")
message = st.text_area("일정 요청", value="민수, 지영과 내일 30분 회의 잡아줘")

if st.button("에이전트 실행"):
    st.info("TODO: requests.post로 backend /agent/schedule API를 호출하세요.")
    st.write(
        {
            "backend_url": backend_url,
            "message": message,
            "next_step": "frontend/app.py에서 API 호출 코드를 구현합니다.",
        }
    )
