r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\03_chain-and-runnable

실행 명령:
    python .\01_simple-runnable-chain.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""RunnableLambda를 사용해 LLM 없이 체인 구조를 이해하는 예제입니다."""

from langchain_core.runnables import RunnableLambda


# RunnableLambda는 일반 Python 함수를 Runnable로 바꿔줍니다.
strip_text = RunnableLambda(lambda text: text.strip())
to_upper = RunnableLambda(lambda text: text.upper())
add_prefix = RunnableLambda(lambda text: f"RESULT: {text}")

# | 연산자로 여러 실행 단계를 순서대로 연결합니다.
chain = strip_text | to_upper | add_prefix

result = chain.invoke("   langchain runnable basic   ")
print(result)
