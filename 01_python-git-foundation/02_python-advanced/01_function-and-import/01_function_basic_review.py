r"""함수 기본 복습 예제입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\01_function-and-import\01_function_basic_review.py

이 예제의 목표:
    1. 함수를 왜 만드는지 이해합니다.
    2. 함수에 값을 전달하고 결과를 return으로 받습니다.
    3. 이후 FastAPI endpoint 안에서도 작은 함수로 로직을 나눌 준비를 합니다.
"""

from myteam.llm import build_chat_response as chat_response

def normalize_question(question: str) -> str:
    """질문 앞뒤의 공백을 제거합니다.

    question:
        사용자가 입력한 원본 질문입니다.

    return:
        앞뒤 공백이 제거된 질문 문자열입니다.
    """

    return question.strip()


def make_mock_answer(question: str) -> str:
    """실제 AI 호출 대신 연습용 답변을 만듭니다."""

    return f"'{question}'에 대한 연습용 답변입니다."



def main() -> None:
    """프로그램 실행 시작점입니다."""
    while True:
        # y/n 입력을 받습니다.n이면 프로그램을 종료합니다. 
        # 나머지는 다시 입력해달라고 안내합니다.
        user_input = input("계속 진행하시겠습니까? (y/n): ")
        if user_input.lower() == "n":
            print("프로그램을 종료합니다.")
            break
        elif user_input.lower() != "y":
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")
            continue

        # msg = "  FastAPI는 무엇인가요?  "
        msg = input("질문을 입력하세요: ")

        if msg == "":
            print("질문이 비어있습니다. 다시 입력해주세요.")
            continue

        request_data = {
            "user": "kim",
            "message": f"{msg}",
            "model": "gpt5.0",
        }

        response = chat_response(request_data)
        cleaned_question = response["message"].strip()

        print("원본 질문:", msg)
        print("정리된 질문:", cleaned_question)

        answer = response["answer"]

        print("답변:", answer)


main()
