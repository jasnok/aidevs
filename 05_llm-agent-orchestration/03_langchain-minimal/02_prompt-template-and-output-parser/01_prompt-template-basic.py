r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\02_prompt-template-and-output-parser

실행 명령:
    python .\01_prompt-template-basic.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""PromptTemplate으로 일반 문자열 프롬프트를 만드는 예제입니다."""

from langchain_core.prompts import PromptTemplate


# PromptTemplate은 반복되는 문장 구조에 입력값만 바꿔 넣을 때 유용합니다.
prompt = PromptTemplate.from_template(
    "{level} 학습자를 위해 {topic} 개념을 쉬운 예시와 함께 설명해줘."
)

formatted_prompt = prompt.invoke({"level": "Python 초보", "topic": "함수"})

print("[생성된 프롬프트]")
print(formatted_prompt.text)
