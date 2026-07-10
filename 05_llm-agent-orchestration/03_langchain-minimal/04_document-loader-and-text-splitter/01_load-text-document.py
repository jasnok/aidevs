r"""실행 안내

실행 위치:
    C:\aidev\05_llm-agent-orchestration\03_langchain-minimal\04_document-loader-and-text-splitter

실행 명령:
    python .\01_load-text-document.py

준비:
    각 단원 README의 가상환경, .env, Docker 실행 안내를 먼저 확인하세요.
"""
"""텍스트 파일을 LangChain Document 객체로 읽어보는 예제입니다."""

from pathlib import Path

from langchain_core.documents import Document


CURRENT_DIR = Path(__file__).resolve().parent
file_path = CURRENT_DIR / "sample_policy.md"

# 간단한 실습에서는 별도 loader 없이 파일을 읽고 Document 객체를 직접 만들 수 있습니다.
if file_path.exists():
    text = file_path.read_text(encoding="utf-8")
    source = file_path.name
else:
    # 문서 정리 후 샘플 Markdown 파일이 없어도 예제가 실행되도록 기본 샘플을 사용합니다.
    text = """
    실습 운영 기준

    학습자는 실습 전에 Python 가상환경을 활성화해야 합니다.
    API Key는 .env 파일에 저장하고 GitHub에 올리지 않습니다.
    Docker 실습은 Docker Desktop이 실행 중일 때만 진행합니다.
    """
    source = "inline_sample_policy"

document = Document(page_content=text, metadata={"source": source})

print("[문서 메타데이터]")
print(document.metadata)
print("\n[문서 앞부분]")
print(document.page_content[:200])
