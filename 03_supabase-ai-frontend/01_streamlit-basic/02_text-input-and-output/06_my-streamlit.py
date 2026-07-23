import streamlit as st

st.title("회원가입")

name = st.text_input("이름을 입력하세요.")

if name:
    st.write(f"안녕하세요 {name}님!")
else:
    st.success("이름을 입력하면 인사말이 표시됩니다.")
    
introduce = st.text_area("자기소개를 입력하세요.")

if introduce:
    st.write(f"{introduce}")
else:
    st.success("자기소개를 입력하면 자기소개 내용이 표시됩니다.")