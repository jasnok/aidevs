r"""dict 데이터를 함수에 전달하는 예제입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\01_function-and-import\02_dict_parameter.py

이 예제의 목표:
    FastAPI, Supabase, LLM API에서는 dict 형태의 데이터를 자주 다룹니다.
    이 예제에서는 dict에서 필요한 값을 꺼내 함수 안에서 처리합니다.
"""


def build_chat_response(request_data: dict) -> dict:
    """질문 dict를 받아 응답 dict를 만듭니다.

    request_data 예시:
        {
            "user": "kim",
            "message": "FastAPI란?",
            "model": "practice-model"
        }
    """

    user = request_data.get("user", "anonymous")
    message = request_data.get("message", "").strip()
    model = request_data.get("model", "practice-model")

    return {
        "user": user,
        "message": message,
        "model": model,
        "answer": f"{user}님, '{message}'에 대한 연습용 답변입니다.",
    }


def main() -> None:
    request_data = {
        "user": "kim",
        "message": "  Python dict는 어디에 쓰나요?  ",
        "model": "practice-model",
    }

    response = build_chat_response(request_data)

    print("요청 dict:")
    print(request_data)
    print()
    print("응답 dict:")
    print(response)


main()
