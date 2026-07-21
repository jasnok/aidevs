from fastapi.testclient import TestClient

from app.main import app
from app.schemes.chat_scheme import ChatResponse


client = TestClient(app)


def test_chat_gemini_returns_answer(monkeypatch):
    """Gemini를 실제 호출하지 않고 채팅 라우터의 요청/응답을 검사한다."""

    def fake_call_gemini(chat_request):
        assert chat_request.user_id == "id01"
        assert chat_request.prompt == "안녕?"
        return ChatResponse(answer="안녕하세요!")

    monkeypatch.setattr(
        "app.routers.chat_router.call_gemini",
        fake_call_gemini,
    )

    response = client.post(
        "/chat/gemini",
        json={"user_id": "id01", "prompt": "안녕?"},
    )

    assert response.status_code == 200
    assert response.json() == {"answer": "안녕하세요!"}


def test_chat_gemini_rejects_empty_prompt():
    """빈 prompt는 Pydantic 검증에서 거부되어야 한다."""

    response = client.post(
        "/chat/gemini",
        json={"user_id": "id01", "prompt": ""},
    )

    assert response.status_code == 422

