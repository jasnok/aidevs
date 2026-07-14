r"""01_simple_chat_project의 기본 서비스 함수 테스트입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python -m pytest .\02_python-advanced\04_project-structure\01_simple_chat_project

이 테스트의 목적:
    create_chat_message 함수가 ChatMessage object를 잘 만드는지 확인합니다.
    아직 저장 기능이나 예외 처리는 테스트하지 않습니다.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# 여러 예제 프로젝트를 한 번에 테스트할 때 이전에 불러온 app 패키지와 섞이지 않게 합니다.
for module_name in list(sys.modules):
    if module_name == "app" or module_name.startswith("app."):
        del sys.modules[module_name]

from app.services import create_chat_message, create_mock_answer


def test_create_mock_answer_contains_question() -> None:
    answer = create_mock_answer("FastAPI란?")

    assert "FastAPI란?" in answer
    assert "연습 답변" in answer


def test_create_chat_message_returns_object() -> None:
    message = create_chat_message("프로젝트 구조란?")

    assert message.question == "프로젝트 구조란?"
    assert "프로젝트 구조란?" in message.answer
    assert message.model == "practice-model"
