import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.


def call_chat_api(message):
    """05_ai-chatbot-interface 샘플 백엔드의 mock chat API를 호출합니다."""
    payload = {"question": message}  # 샘플 백엔드는 question 필드로 사용자 질문을 받습니다.
    response = httpx.post(f"{API_BASE_URL}/api/chat/mock", json=payload, timeout=5.0)  # mock chat API에 질문을 보냅니다.
    response.raise_for_status()  # HTTP 상태 코드가 4xx/5xx이면 예외를 발생시켜 실패를 명확히 처리합니다.
    return response.json()["answer"]  # 응답 JSON에서 assistant 답변 문자열만 꺼내 화면 코드로 돌려줍니다.


st.title("백엔드 mock 챗 API 클라이언트")  # Streamlit 화면의 가장 큰 제목을 표시합니다.
st.caption("05_ai-chatbot-interface/00_sample_backend의 /api/chat/mock 엔드포인트를 호출합니다.")  # 호출 대상을 화면에 안내합니다.

prompt = st.chat_input("질문을 입력하세요")  # 채팅 입력창에서 사용자가 보낸 질문 문자열을 변수에 저장합니다.

if prompt:  # 사용자가 채팅 입력창에 질문을 입력했을 때만 메시지 처리 로직을 실행합니다.
    st.chat_message("user").write(prompt)  # 사용자 질문을 user 말풍선에 출력합니다.
    with st.spinner("mock 백엔드 응답을 기다리는 중입니다..."):  # API 응답을 기다리는 동안 로딩 메시지를 보여줍니다.
        reply = call_chat_api(prompt)  # 백엔드 mock API가 만든 응답 문자열을 화면 출력용 변수에 저장합니다.
    st.chat_message("assistant").write(reply)  # assistant 답변을 assistant 말풍선에 출력합니다.
