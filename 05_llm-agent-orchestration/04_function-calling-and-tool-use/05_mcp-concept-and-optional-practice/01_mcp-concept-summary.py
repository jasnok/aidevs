r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\04_function-calling-and-tool-use\05_mcp-concept-and-optional-practice

실행 명령:
    python .\01_mcp-concept-summary.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""MCP 개념을 초보자용 표 형태로 정리하는 예제입니다."""

concepts = [
    {
        "keyword": "Function Calling",
        "meaning": "LLM이 애플리케이션 함수 호출을 요청하는 방식",
        "practice": "Python 함수와 JSON schema를 직접 연결한다.",
    },
    {
        "keyword": "Tool Use",
        "meaning": "LLM이 외부 기능을 도구처럼 사용하는 넓은 개념",
        "practice": "API, DB, 검색, 계산 기능을 도구로 제공한다.",
    },
    {
        "keyword": "MCP",
        "meaning": "모델과 도구를 더 표준화된 방식으로 연결하기 위한 프로토콜",
        "practice": "선택 확장으로 개념을 이해하고 이후 실습에서 다룬다.",
    },
]

for concept in concepts:
    print(f"[{concept['keyword']}]")
    print("의미:", concept["meaning"])
    print("실습 적용:", concept["practice"])
    print()
