# 01 Embedding Basics

이 폴더에서는 문장을 숫자 벡터로 바꾸는 임베딩의 기초를 학습합니다.

## 핵심 개념

- 임베딩은 텍스트의 의미를 숫자 목록으로 표현합니다.
- 의미가 비슷한 문장은 벡터 공간에서 가까운 위치에 놓입니다.
- 벡터 유사도는 RAG 검색의 출발점입니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_vector-similarity-basic.py` | API 없이 간단한 숫자 벡터로 유사도 계산 흐름을 확인합니다. |
| `02_openai-embedding-basic.py` | OpenAI 임베딩 API를 사용해 실제 문장을 벡터로 변환합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python .\01_embedding-basics\01_vector-similarity-basic.py
python .\01_embedding-basics\02_openai-embedding-basic.py
```

## 확인 질문

- 문장을 숫자로 바꾸면 어떤 비교가 가능해지는가?
- 유사도 점수가 높다는 것은 무엇을 의미하는가?
- RAG에서 임베딩이 필요한 이유는 무엇인가?
