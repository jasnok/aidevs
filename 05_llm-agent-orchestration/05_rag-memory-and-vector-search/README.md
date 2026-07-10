# 05 RAG Memory and Vector Search

이 단원에서는 LLM이 직접 알고 있지 않은 자료를 검색해서 답변에 활용하는 RAG 구조를 학습합니다.

핵심 흐름은 다음과 같습니다.

```text
문서 준비 -> 문서 청킹 -> 임베딩 생성 -> pgvector 저장 -> 관련 문서 검색 -> LLM 답변 생성 -> 대화 기억 저장 -> Redis 캐시 확인
```

05 과정부터는 Supabase가 아니라 Docker 기반 로컬 실습을 사용합니다. 이 단원에서는 Docker Desktop에서 `pgvector`가 포함된 PostgreSQL 컨테이너를 실행하고, 그 안에 벡터 데이터를 저장합니다. Docker Compose와 AWS 배포는 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 학습 목표

- 임베딩이 텍스트를 숫자 벡터로 바꾸는 이유를 이해합니다.
- 벡터 유사도를 이용해 질문과 관련 있는 문서를 찾습니다.
- Docker로 실행한 pgvector PostgreSQL에 문서 벡터를 저장하고 검색합니다.
- 문서 청킹 크기와 overlap이 검색 품질에 주는 영향을 확인합니다.
- RAG, Hybrid Search, RRF, RAG 품질 평가의 기본 흐름을 실습합니다.
- PostgreSQL Session Memory와 Redis Cache의 역할을 구분합니다.
- Session Memory와 Long-term Memory의 차이를 구분합니다.

## 폴더 구성

```text
05_rag-memory-and-vector-search
├─ .env.example
├─ README.md
├─ 00_references
│  └─ README.md
├─ 01_embedding-basics
│  ├─ README.md
│  ├─ 01_vector-similarity-basic.py
│  └─ 02_openai-embedding-basic.py
├─ 02_pgvector-basic
│  ├─ README.md
│  ├─ 01_create-extension-and-tables.sql
│  ├─ 01_insert-sample-vectors.py
│  ├─ 02_sample-vector-search.sql
│  └─ 02_search-similar-vectors.py
├─ 03_document-chunking-and-indexing
│  ├─ README.md
│  ├─ 01_split-sample-document.py
│  └─ 02_index-document-chunks.py
├─ 04_rag-retrieval-and-answering
│  ├─ README.md
│  ├─ 01_retrieve-context.py
│  ├─ 02_rag-answer.py
│  ├─ 03_hybrid-search-rrf.py
│  └─ 04_rag-quality-evaluation.py
├─ 05_conversation-memory
│  ├─ README.md
│  ├─ 01_short-term-memory.py
│  ├─ 02_save-conversation-memory.py
│  ├─ 03_load-recent-session-messages.py
│  └─ 04_redis-session-cache.py
├─ 10_labs
└─ 20_assignments
```

## 실습 환경 준비

```powershell
cd C:\aidev\05_llm-agent-orchestration\05_rag-memory-and-vector-search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv psycopg[binary] redis langchain-text-splitters
Copy-Item .env.example .env
```

`.env` 파일은 이 단원 폴더 안의 파일을 사용합니다. 다른 과정의 `.env`를 그대로 복사하지 말고, 이 단원의 `.env.example`을 기준으로 필요한 값을 채웁니다.

## pgvector 컨테이너 실행

Docker Desktop을 켠 뒤 아래 명령을 실행합니다.

```powershell
docker run -d `
  --name aidev-pgvector `
  -e POSTGRES_DB=agent_db `
  -e POSTGRES_USER=agent_user `
  -e POSTGRES_PASSWORD=agent_password `
  -p 5433:5432 `
  -v aidev-pgvector-data:/var/lib/postgresql/data `
  pgvector/pgvector:pg16
```

컨테이너가 실행 중인지 확인합니다.

```powershell
docker ps
docker exec -it aidev-pgvector psql -U agent_user -d agent_db
```

`psql` 화면에 들어가면 `\q`를 입력해서 빠져나옵니다.

## Redis 컨테이너 실행

세션 캐시와 짧은 기억 실습을 위해 Redis를 실행합니다.

```powershell
docker run -d `
  --name aidev-redis `
  -p 6379:6379 `
  redis:7
```

동작 확인:

```powershell
docker exec -it aidev-redis redis-cli ping
```

정상이라면 `PONG`이 출력됩니다.

## 실행 순서

API Key나 DB 없이 먼저 실행할 수 있는 예제입니다.

```powershell
python .\01_embedding-basics\01_vector-similarity-basic.py
python .\03_document-chunking-and-indexing\01_split-sample-document.py
python .\04_rag-retrieval-and-answering\03_hybrid-search-rrf.py
python .\04_rag-retrieval-and-answering\04_rag-quality-evaluation.py
python .\05_conversation-memory\01_short-term-memory.py
```

OpenAI API Key와 pgvector 컨테이너가 준비되면 DB 연동 예제를 실행합니다.

```powershell
Get-Content .\02_pgvector-basic\01_create-extension-and-tables.sql | docker exec -i aidev-pgvector psql -U agent_user -d agent_db
python .\02_pgvector-basic\01_insert-sample-vectors.py
python .\02_pgvector-basic\02_search-similar-vectors.py
python .\03_document-chunking-and-indexing\02_index-document-chunks.py
python .\04_rag-retrieval-and-answering\01_retrieve-context.py
python .\04_rag-retrieval-and-answering\02_rag-answer.py
python .\05_conversation-memory\02_save-conversation-memory.py
python .\05_conversation-memory\03_load-recent-session-messages.py
python .\05_conversation-memory\04_redis-session-cache.py
```

## 단원별 핵심 질문

| 폴더 | 핵심 질문 |
| --- | --- |
| `01_embedding-basics` | 문장을 숫자 벡터로 바꾸면 어떤 비교가 가능해지는가? |
| `02_pgvector-basic` | PostgreSQL에 벡터를 저장하면 일반 검색과 무엇이 달라지는가? |
| `03_document-chunking-and-indexing` | chunk 크기와 overlap은 검색 품질에 어떤 영향을 주는가? |
| `04_rag-retrieval-and-answering` | 검색된 context가 답변 품질과 근거성에 어떤 영향을 주는가? |
| `05_conversation-memory` | Session Memory와 Long-term Memory는 각각 어떤 문제를 해결하는가? |

## 산출물 기준

- pgvector 컨테이너 실행 화면 또는 `docker ps` 확인 결과
- 벡터 검색 결과와 검색 기준 설명
- RAG 답변 결과와 사용된 context 설명
- 메모리 저장 구조 요약
- 실습 중 발생한 오류와 해결 방법 기록
