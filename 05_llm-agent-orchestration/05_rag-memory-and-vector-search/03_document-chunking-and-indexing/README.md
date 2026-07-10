# 03 Document Chunking and Indexing

이 폴더에서는 긴 문서를 작은 조각으로 나누고, 각 조각을 임베딩해 검색 가능한 형태로 저장합니다.

## 핵심 개념

- 긴 문서는 한 번에 검색하기 어렵기 때문에 chunk로 나눕니다.
- chunk마다 임베딩을 생성하면 질문과 가장 관련 있는 문서 조각을 찾을 수 있습니다.
- chunk 크기와 overlap 설정은 검색 품질에 큰 영향을 줍니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_split-sample-document.py` | 샘플 문서를 chunk로 나누는 과정을 확인합니다. |
| `02_index-document-chunks.py` | chunk를 임베딩해서 pgvector에 저장합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python .\03_document-chunking-and-indexing\01_split-sample-document.py
python .\03_document-chunking-and-indexing\02_index-document-chunks.py
```

## 확인 질문

- chunk를 너무 작게 나누면 어떤 문제가 생기는가?
- chunk를 너무 크게 나누면 어떤 문제가 생기는가?
- overlap은 어떤 상황에서 도움이 되는가?
