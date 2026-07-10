# 04 RAG Retrieval and Answering

이 폴더에서는 검색된 문서 조각을 LLM에 전달하여 근거 기반 답변을 생성합니다.

## 핵심 개념

- Retrieval은 질문과 관련 있는 문서를 찾는 단계입니다.
- Generation은 검색 결과를 context로 사용해 답변을 만드는 단계입니다.
- Hybrid Search는 키워드 검색과 벡터 검색을 함께 사용합니다.
- RAG 품질 평가는 답변이 근거에 충실한지 확인하는 과정입니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_retrieve-context.py` | 질문에 맞는 context를 검색합니다. |
| `02_rag-answer.py` | 검색된 context를 LLM에 전달해 답변을 생성합니다. |
| `03_hybrid-search-rrf.py` | 키워드 검색과 벡터 검색 결과를 RRF로 결합합니다. |
| `04_rag-quality-evaluation.py` | RAG 답변 품질을 간단한 기준으로 평가합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python .\04_rag-retrieval-and-answering\01_retrieve-context.py
python .\04_rag-retrieval-and-answering\02_rag-answer.py
python .\04_rag-retrieval-and-answering\03_hybrid-search-rrf.py
python .\04_rag-retrieval-and-answering\04_rag-quality-evaluation.py
```

## 확인 질문

- 검색된 context를 제공하면 LLM 답변이 어떻게 달라지는가?
- RRF는 여러 검색 결과를 어떻게 합치는가?
- RAG 답변의 품질은 어떤 기준으로 볼 수 있는가?
