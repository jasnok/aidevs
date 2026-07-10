import httpx  # FastAPI 같은 백엔드 API에 HTTP 요청을 보내기 위해 httpx 클라이언트를 가져옵니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

API_BASE_URL = "http://127.0.0.1:8000"  # 프론트엔드가 호출할 백엔드 서버의 기본 주소를 한 곳에서 관리합니다.

st.title("과정 목록 조회")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

if st.button("과정 목록 불러오기"):  # 버튼을 누른 순간에만 과정 목록 API를 호출합니다.
    response = httpx.get(f"{API_BASE_URL}/api/courses", timeout=5.0)  # 과정 목록을 조회하는 GET 요청을 보냅니다.
    data = response.json()  # JSON 응답을 딕셔너리로 변환합니다.
    courses = data.get("courses", [])  # courses key가 없을 때를 대비해 기본값으로 빈 리스트를 사용합니다.

    st.write("과정 목록")  # 아래 출력이 어떤 데이터인지 설명합니다.
    for course in courses:  # 과정 목록을 하나씩 꺼내 화면에 표시합니다.
        st.write(f"- {course}")  # 각 과정을 목록처럼 출력합니다.
