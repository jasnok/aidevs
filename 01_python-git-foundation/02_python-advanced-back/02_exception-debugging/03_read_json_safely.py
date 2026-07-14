r"""JSON 파일을 안전하게 읽는 예제입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\02_exception-debugging\03_read_json_safely.py

이 예제의 목표:
    1. JSON 파일을 읽습니다.
    2. 파일이 없을 때의 오류를 처리합니다.
    3. JSON 문법이 깨졌을 때의 오류를 처리합니다.
"""

import json
from pathlib import Path


CURRENT_DIR = Path(__file__).parent


def read_json_safely(file_name: str) -> dict:
    """JSON 파일을 읽고 dict로 반환합니다.

    오류가 나면 프로그램을 바로 종료하지 않고 빈 dict를 반환합니다.
    """

    file_path = CURRENT_DIR / file_name

    try:
        text = file_path.read_text(encoding="utf-8")
        return json.loads(text)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return {}
    except json.JSONDecodeError as error:
        print(f"JSON 문법이 올바르지 않습니다: {file_path}")
        print("오류 위치:", error)
        return {}


def main() -> None:
    for file_name in ["config.json", "missing.json", "broken_config.json"]:
        print()
        print("읽는 파일:", file_name)
        config = read_json_safely(file_name)
        print("읽은 결과:", config)


main()
