r"""01_simple_chat_project의 실행 시작점입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\04_project-structure\01_simple_chat_project\main.py

이 파일의 역할:
    1. 예제 질문을 준비합니다.
    2. services.py의 함수로 질문과 답변 데이터를 만듭니다.
    3. 만들어진 결과를 화면에 출력합니다.

중요:
    이 예제는 프로젝트 구조를 익히기 위한 첫 단계입니다.
    그래서 JSON 저장, 빈 질문 검증, 예외 처리는 아직 넣지 않습니다.
"""

from app.services import create_chat_message


def main() -> None:
    question = "프로젝트 구조는 왜 나누나요?"

    message = create_chat_message(question)

    print("질문:")
    print(message.question)
    print()
    print("답변:")
    print(message.answer)
    print()
    print("사용 모델:")
    print(message.model)


main()
