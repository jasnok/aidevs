import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("버튼 클릭 예제")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

message_col, alert_col = st.columns(2)  # 버튼 두 개를 나란히 배치하기 위해 화면을 두 칸으로 나눕니다.

with message_col:
    clicked = st.button("인사말 보기")  # 버튼을 누르면 True, 누르지 않으면 False가 됩니다.

with alert_col:
    alert_clicked = st.button("알림 보기")  # 알림을 띄울지 판단하기 위한 버튼입니다.

if alert_clicked:  # 알림 보기 버튼을 클릭했을 때 실행합니다.
    # Streamlit에서는 브라우저 alert() 대신 st.toast()를 자주 사용합니다.
    # toast는 화면 오른쪽 위에 잠깐 나타나는 알림 메시지입니다.
    st.toast("알림 버튼이 클릭되었습니다.")

if clicked:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    st.success("안녕하세요. 버튼이 클릭되었습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
    st.info("버튼을 클릭하면 메시지 또는 알림이 표시됩니다.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

