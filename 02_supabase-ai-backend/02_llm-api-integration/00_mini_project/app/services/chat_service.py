# chat_service.py
import os
from app.schemes.chat_scheme import ChatResponse, ChatRequest
from google import genai


def call_gemini(chat_request:ChatRequest):

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

 
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=chat_request.prompt,
    )

    return ChatResponse(
        answer= response.text
    )