r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\04_document-loader-and-text-splitter

실행 명령:
    python .\02_split-documents.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""문서를 작은 chunk로 나누는 예제입니다."""

from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


CURRENT_DIR = Path(__file__).resolve().parent
file_path = CURRENT_DIR / "sample_policy.md"

if file_path.exists():
    text = file_path.read_text(encoding="utf-8")
    source = file_path.name
else:
    # 문서 정리 후 샘플 Markdown 파일이 없어도 chunk 분할 흐름을 볼 수 있게 합니다.
    text = """
    실습 운영 기준

    학습자는 실습 전에 Python 가상환경을 활성화해야 합니다.
    API Key는 .env 파일에 저장하고 GitHub에 올리지 않습니다.
    Docker 실습은 Docker Desktop이 실행 중일 때만 진행합니다.
    오류가 발생하면 현재 폴더, 가상환경, 환경 변수, Docker 실행 상태를 순서대로 확인합니다.
    """
    source = "inline_sample_policy"

document = Document(page_content=text, metadata={"source": source})

# chunk_size는 한 조각의 최대 길이, chunk_overlap은 조각 사이에 겹치는 길이입니다.
splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=20)
chunks = splitter.split_documents([document])

print(f"총 chunk 수: {len(chunks)}")
for index, chunk in enumerate(chunks, start=1):
    print(f"\n--- chunk {index} ---")
    print(chunk.page_content)
    print("metadata:", chunk.metadata)
