-- 주의:
-- 이 SQL은 실습을 처음부터 다시 시작하기 위해 기존 테이블을 삭제하고 다시 만듭니다.
-- 이미 저장한 벡터, 문서 chunk, 대화 메모리 데이터가 있다면 사라질 수 있습니다.
-- 05 과정에서는 docker run으로 실행한 aidev-pgvector 컨테이너에 이 SQL을 적용합니다.

CREATE EXTENSION IF NOT EXISTS vector;

DROP TABLE IF EXISTS conversation_messages;
DROP TABLE IF EXISTS document_chunks;
DROP TABLE IF EXISTS sample_vectors;

CREATE TABLE sample_vectors (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(3) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE document_chunks (
    id BIGSERIAL PRIMARY KEY,
    document_title TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE conversation_messages (
    id BIGSERIAL PRIMARY KEY,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_document_chunks_embedding
ON document_chunks
USING hnsw (embedding vector_cosine_ops);
