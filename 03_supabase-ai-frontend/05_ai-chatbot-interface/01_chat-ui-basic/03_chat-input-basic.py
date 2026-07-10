import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("채팅 입력 기본")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

prompt = st.chat_input("질문을 입력하세요")  # 채팅 입력창에서 사용자가 보낸 질문 문자열을 변수에 저장합니다.

if prompt:  # 사용자가 채팅 입력창에 질문을 입력했을 때만 메시지 처리 로직을 실행합니다.
    with st.chat_message("user"):  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
        st.write(prompt)  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.

    with st.chat_message("assistant"):  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
        st.write("입력한 질문을 확인했습니다.")  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.info("아래 입력창에 질문을 입력해 보세요.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.


