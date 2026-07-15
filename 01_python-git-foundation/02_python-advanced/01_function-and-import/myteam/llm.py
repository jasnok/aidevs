def build_chat_response(request_data: dict) -> dict:
    """사용자 요청 데이터를 받아서 챗봇 응답을 만듭니다.

    request_data:
        사용자 요청 데이터입니다. 예시:
        {
            "user": "kim",
            "message": "FastAPI는 무엇인가요?",
            "model": "gpt5.0",
        }

    return:
        챗봇 응답 데이터입니다. 예시:
        {
            "user": "kim",
            "message": "FastAPI는 무엇인가요?",
            "model": "gpt5.0",
            "answer": "'FastAPI는 무엇인가요?'에 대한 연습용 답변입니다."
        }
    """

    print("LLM에 물어보는중 ............")
    print("LLM에 답변을 받았습니다! ............")
    print("요청 dict:", request_data)
    print("응답 dict:", request_data)
    cleaned_question = normalize_question(request_data["message"])
    answer = make_mock_answer(cleaned_question)

    response_data = {
        **request_data,
        "answer": answer,
    }

    return response_data
