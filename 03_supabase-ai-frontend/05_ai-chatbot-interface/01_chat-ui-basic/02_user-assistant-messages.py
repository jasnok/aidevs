import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("역할별 메시지 출력")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

messages = [  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    {"role": "user", "content": "오늘 배울 내용은 무엇인가요?"},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    {"role": "assistant", "content": "Streamlit으로 챗봇 화면을 만드는 방법입니다."},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    {"role": "user", "content": "대화 이력도 저장할 수 있나요?"},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    {"role": "assistant", "content": "네, session_state를 사용하면 가능합니다."},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
]

for message in messages:  # 목록이나 반복 가능한 데이터를 하나씩 꺼내 같은 작업을 반복합니다.
    with st.chat_message(message["role"]):  # 파일, 화면 영역, 로딩 상태처럼 시작과 종료가 있는 작업 범위를 만듭니다.
        st.write(message["content"])  # 문자열, 숫자, 객체를 Streamlit 화면에 출력합니다.


