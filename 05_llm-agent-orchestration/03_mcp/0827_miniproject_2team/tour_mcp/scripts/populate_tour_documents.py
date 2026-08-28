"""기존 호텔·관광지 데이터의 검색 문서와 임베딩을 일괄 적재합니다."""

import sys
from pathlib import Path

from psycopg.types.json import Jsonb


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from mcp_server.tour_database import get_connection  # noqa: E402
from mcp_server.tour_embeddings import (  # noqa: E402
    EMBEDDING_MODEL,
    build_attraction_content,
    build_hotel_content,
    create_content_hash,
    create_embedding,
    vector_literal,
)


HOTEL_QUERY = """
SELECT hotel_id, name, city, district, address, price, rating, review_count,
       hotel_grade, room_type, breakfast_included, parking, wifi, pool,
       description
FROM hotels
ORDER BY hotel_id
"""

ATTRACTION_QUERY = """
SELECT id, city, area, name, address, description, precautions
FROM tourist_attractions
ORDER BY id
"""

EXISTING_QUERY = """
SELECT content_hash, embedding_model
FROM tour_documents
WHERE entity_type = %s AND entity_id = %s
  AND chunk_type = 'summary' AND chunk_index = 0
"""

UPSERT_QUERY = """
INSERT INTO tour_documents (
    entity_type, entity_id, chunk_type, chunk_index, content, metadata,
    embedding, embedding_model, content_hash
)
VALUES (%s, %s, 'summary', 0, %s, %s, %s::vector, %s, %s)
ON CONFLICT (entity_type, entity_id, chunk_type, chunk_index)
DO UPDATE SET
    content = EXCLUDED.content,
    metadata = EXCLUDED.metadata,
    embedding = EXCLUDED.embedding,
    embedding_model = EXCLUDED.embedding_model,
    content_hash = EXCLUDED.content_hash,
    updated_at = CURRENT_TIMESTAMP
"""


def hotel_metadata(row: dict) -> dict:
    return {
        "city": row["city"],
        "district": row.get("district"),
        "price": row["price"],
        "rating": float(row["rating"]) if row.get("rating") is not None else None,
        "hotel_grade": row.get("hotel_grade"),
    }


def attraction_metadata(row: dict) -> dict:
    return {
        "city": row["city"],
        "area": row["area"],
        "name": row["name"],
    }


def sync_rows(entity_type: str, rows: list[dict], content_builder, metadata_builder) -> dict:
    stats = {"success": 0, "skipped": 0, "failed": 0}
    with get_connection() as connection:
        for row in rows:
            entity_id = str(row["hotel_id"] if entity_type == "hotel" else row["id"])
            try:
                content = content_builder(row)
                content_hash = create_content_hash(content)
                with connection.cursor() as cursor:
                    cursor.execute(EXISTING_QUERY, (entity_type, entity_id))
                    existing = cursor.fetchone()
                if (
                    existing
                    and existing["content_hash"] == content_hash
                    and existing["embedding_model"] == EMBEDDING_MODEL
                ):
                    stats["skipped"] += 1
                    continue

                embedding = vector_literal(create_embedding(content))
                with connection.cursor() as cursor:
                    cursor.execute(
                        UPSERT_QUERY,
                        (
                            entity_type,
                            entity_id,
                            content,
                            Jsonb(metadata_builder(row)),
                            embedding,
                            EMBEDDING_MODEL,
                            content_hash,
                        ),
                    )
                connection.commit()
                stats["success"] += 1
            except Exception as exc:
                connection.rollback()
                stats["failed"] += 1
                print(f"[{entity_type}:{entity_id}] 실패: {exc}")
    return stats


def main() -> None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(HOTEL_QUERY)
            hotels = cursor.fetchall()
            cursor.execute(ATTRACTION_QUERY)
            attractions = cursor.fetchall()

    hotel_stats = sync_rows("hotel", hotels, build_hotel_content, hotel_metadata)
    attraction_stats = sync_rows(
        "attraction", attractions, build_attraction_content, attraction_metadata
    )
    print(f"호텔: {hotel_stats}")
    print(f"관광지: {attraction_stats}")


if __name__ == "__main__":
    main()

