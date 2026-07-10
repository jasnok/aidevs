r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\05_conversation-memory

실행 명령:
    python .\01_short-term-memory.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""현재 실행 중인 프로그램 안에서만 유지되는 단기 메모리 예제입니다."""

conversation = []


def add_message(role: str, content: str) -> None:
    """대화 메시지를 메모리 목록에 추가합니다."""
    conversation.append({"role": role, "content": content})


add_message("user", "FastAPI가 뭐야?")
add_message("assistant", "FastAPI는 Python으로 API 서버를 만드는 웹 프레임워크입니다.")
add_message("user", "그럼 Streamlit과 어떻게 연결해?")

print("현재 대화 메모리:")
for message in conversation:
    print(f"{message['role']}: {message['content']}")

print("\n주의: 이 메모리는 프로그램이 종료되면 사라집니다.")
