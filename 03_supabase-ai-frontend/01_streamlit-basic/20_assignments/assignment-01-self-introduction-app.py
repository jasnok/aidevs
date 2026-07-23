import streamlit as st

st.title("자기소개 앱")

name = st.text_input("이름을 입력하세요.")

if name:
    st.write(f"안녕하세요! {name}님!")
else:
    st.success("이름을 입력하면 인사말이 표시됩니다.")

# 관심 분야를 선택받습니다.(st.selectbox)

hobby = st.selectbox("관심 분야를 선택하세요!", ["파이썬","자바","SQL"])
level = st.radio("학습 수준", ["초급","중급","고급"])

# 자기소개 문장을 입력받습니다. (st.text_area)