# 02 Pgvector Basic

이 폴더에서는 Docker로 실행한 pgvector PostgreSQL 컨테이너에 벡터를 저장하고 검색합니다.

## 핵심 개념

- pgvector는 PostgreSQL에서 벡터 저장과 유사도 검색을 가능하게 해주는 확장입니다.
- 이 과정에서는 PostgreSQL을 노트북에 직접 설치하지 않고 Docker 컨테이너로 실행합니다.
- 벡터 검색은 질문과 의미가 가까운 문서를 찾는 데 사용됩니다.

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_create-extension-and-tables.sql` | pgvector 확장과 실습 테이블을 생성합니다. |
| `01_insert-sample-vectors.py` | 샘플 문장을 임베딩한 뒤 DB에 저장합니다. |
| `02_sample-vector-search.sql` | SQL로 벡터 검색 구조를 확인합니다. |
| `02_search-similar-vectors.py` | Python에서 질문과 가까운 문서를 검색합니다. |

## 실행

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
Get-Content .\02_pgvector-basic\01_create-extension-and-tables.sql | docker exec -i aidev-pgvector psql -U agent_user -d agent_db
python .\02_pgvector-basic\01_insert-sample-vectors.py
python .\02_pgvector-basic\02_search-similar-vectors.py
```

## 확인 질문

- pgvector는 일반 PostgreSQL과 무엇이 다른가?
- 벡터 검색 결과는 어떤 기준으로 정렬되는가?
- DB에 저장할 원문과 벡터를 함께 보관해야 하는 이유는 무엇인가?
