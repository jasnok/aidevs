r"""백엔드의 Gemini chat API를 호출하는 Streamlit 예제입니다.

실행 전 준비:
    1. 05_ai-chatbot-interface/00_sample_backend/.env에 GEMINI_API_KEY를 설정합니다.
    2. 05_ai-chatbot-interface/00_sample_backend를 먼저 실행합니다.

백엔드 실행:
    cd C:\aidev\03_supabase-ai-frontend
    .\.venv\Scripts\Activate.ps1
    cd .\05_ai-chatbot-interface\00_sample_backend
    uvicorn main:app --reload --host 127.0.0.1 --port 8000

프론트엔드 실행:
    cd C:\aidev\03_supabase-ai-frontend
    .\.venv\Scripts\Activate.ps1
    streamlit run .\05_ai-chatbot-interface\04_mock-and-optional-gemini-interface\06_backend-gemini-chat-client.py
"""

import os  # API_BASE_URL을 환경변수에서 읽기 위해 사용합니다.

import httpx  # FastAPI 백엔드 API에 HTTP 요청을 보내기 위해 사용합니다.
import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.


API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
CHAT_ENDPOINT = "/api/chat/gemini"


def call_gemini_chat_api(message):
    """FastAPI 백엔드의 Gemini chat API를 호출합니다."""

    # 이 함수는 Gemini SDK를 직접 import하지 않습니다.
    # Streamlit은 질문만 백엔드로 보내고, Gemini API key와 실제 호출은 백엔드가 처리합니다.
    payload = {"question": message}
    response = httpx.post(f"{API_BASE_URL}{CHAT_ENDPOINT}", json=payload, timeout=30.0)
    response.raise_for_status()
    return response.json()


st.title("백엔드 Gemini 챗 API 클라이언트")
st.caption("Streamlit은 Gemini를 직접 호출하지 않고, FastAPI 백엔드의 /api/chat/gemini를 호출합니다.")
st.code(f"POST {API_BASE_URL}{CHAT_ENDPOINT}", language="text")

prompt = st.chat_input("Gemini에게 보낼 질문을 입력하세요")

if prompt:
    st.chat_message("user").write(prompt)

    try:
        with st.spinner("백엔드에서 Gemini 응답을 생성하는 중입니다..."):
            result = call_gemini_chat_api(prompt)

        st.chat_message("assistant").write(result["answer"])
        st.caption(f"provider={result['provider']} | model={result['model']} | actual_api_called={result['actual_api_called']}")

    except httpx.ConnectError:
        st.error("챗봇 백엔드에 연결할 수 없습니다. 05_ai-chatbot-interface/00_sample_backend를 먼저 실행하세요.")
    except httpx.TimeoutException:
        st.error("Gemini 응답 시간이 초과되었습니다. 잠시 후 다시 시도하세요.")
    except httpx.HTTPStatusError as error:
        detail = error.response.text
        st.error(f"백엔드 API 오류가 발생했습니다. status={error.response.status_code}")
        st.code(detail, language="json")
