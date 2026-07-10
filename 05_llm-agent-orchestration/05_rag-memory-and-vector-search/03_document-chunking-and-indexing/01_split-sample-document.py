r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search\03_document-chunking-and-indexing

실행 명령:
    python .\01_split-sample-document.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""샘플 문서를 chunk로 나누는 예제입니다."""

from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


CURRENT_DIR = Path(__file__).resolve().parent
sample_path = CURRENT_DIR / "sample_course_guide.md"

if sample_path.exists():
    text = sample_path.read_text(encoding="utf-8")
else:
    # 문서 정리 후 샘플 Markdown 파일이 없어도 chunk 분할 개념을 실습할 수 있게 합니다.
    text = """
    05 LLM Agent Orchestration 과정은 Prompt, Tool Calling, RAG, Memory, LangGraph를 순서대로 학습합니다.
    학습자는 먼저 LLM 호출 방식을 이해하고, 이후 Python 함수 Tool을 설계합니다.
    RAG 단원에서는 문서를 chunk로 나누고 embedding으로 변환한 뒤 pgvector에 저장합니다.
    LangGraph 단원에서는 Agent의 상태를 State로 관리하고 Node와 Edge로 실행 흐름을 구성합니다.
    Docker Compose와 AWS 배포는 07 과정에서 다룹니다.
    """

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=60)
chunks = splitter.split_text(text)

print(f"총 chunk 수: {len(chunks)}")
for index, chunk in enumerate(chunks, start=1):
    print(f"\n--- chunk {index} ---")
    print(chunk)
