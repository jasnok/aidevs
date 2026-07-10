"""Chat 탭입니다."""

import streamlit as st

from frontend_common import require_login


def render_chat_tab() -> None:
    """로그인 후 mock 대화를 입력하고 누적 표시합니다."""

    st.subheader("Chat")
    st.caption("로그인 후 mock 대화를 입력하고 누적 표시합니다.")

    with st.form("chat_form", clear_on_submit=True):
        message = st.text_input("메시지 입력", placeholder="오늘 배운 내용을 정리해줘.")
        submitted = st.form_submit_button("전송")

    if submitted:
        message = message.strip()
        if not message:
            st.warning("메시지를 입력하세요.")
        elif require_login():
            st.session_state["chat_messages"].append({"role": "user", "content": message})
            st.session_state["chat_messages"].append(
                {
                    "role": "assistant",
                    "content": f"'{message}'에 대한 mock 답변입니다. 실제 API 연결은 99 최종 프로젝트에서 확인합니다.",
                }
            )

    st.divider()
    st.subheader("대화 내용")

    if not st.session_state["chat_messages"]:
        st.info("아직 대화가 없습니다.")
        return

    for item in st.session_state["chat_messages"]:
        st.chat_message(item["role"]).write(item["content"])
