# 04_document-loader-and-text-splitter

이 챕터에서는 문서를 읽고 작은 chunk로 나누는 RAG 전처리 과정을 학습합니다.

## 핵심 개념

- LLM에게 긴 문서를 한 번에 모두 넣기 어렵습니다.
- 문서를 작은 chunk로 나누면 검색과 요약에 유리합니다.
- chunk overlap은 문맥이 끊기는 문제를 줄이는 데 사용합니다.

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\03_langchain-minimal
.\.venv\Scripts\Activate.ps1
python .\04_document-loader-and-text-splitter\01_load-text-document.py
python .\04_document-loader-and-text-splitter\02_split-documents.py
```

## 확인 질문

- 문서를 chunk로 나누는 이유는 무엇인가요?
- chunk 크기가 너무 작거나 크면 어떤 문제가 생길까요?

