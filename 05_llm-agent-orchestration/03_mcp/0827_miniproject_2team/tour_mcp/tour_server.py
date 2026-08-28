"""대한민국 호텔·관광지 Streamable HTTP MCP Server."""

import os

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from pathlib import Path

try:
    from .tour_database import fetch_all
    from .tour_embeddings import create_embedding, vector_literal
except ImportError:  # python mcp_server/tour_server.py 직접 실행 지원
    from tour_database import fetch_all
    from tour_embeddings import create_embedding, vector_literal

# ROOT = Path(__file__).resolve().parents[1]
# load_dotenv(ROOT / ".env")

load_dotenv()

MCP_HOST = os.getenv("TOUR_MCP_HOST", "127.0.0.1")
MCP_PORT = int(os.getenv("TOUR_MCP_PORT", "8020"))
MAX_RESULT_COUNT = 20

mcp = FastMCP(
    "mini-agent-tour",
    instructions=(
        "대한민국 내 호텔과 관광지 명소 정보를 제공합니다. "
        "지역, 가격 및 자연어 조건으로 호텔과 관광지를 검색하며, "
        "관광지 주변 호텔을 추천할 수 있습니다."
    ),
    host=MCP_HOST,
    port=MCP_PORT,
    stateless_http=True,
    json_response=True,
)


def required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name}은 빈 문자열일 수 없습니다.")
    return normalized


def validate_options(max_price: int | None, count: int) -> None:
    if max_price is not None and max_price < 1:
        raise ValueError("max_price는 1 이상이어야 합니다.")
    if count < 1 or count > MAX_RESULT_COUNT:
        raise ValueError(f"count는 1 이상 {MAX_RESULT_COUNT} 이하여야 합니다.")


HOTEL_COLUMNS = """
h.hotel_id, h.name, h.city, h.district, h.address, h.price, h.rating,
h.review_count, h.hotel_grade, h.room_type, h.breakfast_included,
h.parking, h.wifi, h.pool, h.description
"""


@mcp.tool()
def search_hotels(
    region: str,
    max_price: int | None = None,
    count: int = 5,
    query: str = "",
) -> dict:
    """지역·선택적 최대 가격으로 호텔을 검색하며 count 기본값은 5입니다."""
    region = required_text(region, "region")
    query = query.strip()
    validate_options(max_price, count)

    if query:
        query_vector = vector_literal(create_embedding(query))
        items = fetch_all(
            f"""
            SELECT {HOTEL_COLUMNS},
                   1 - (d.embedding <=> %s::vector) AS similarity
            FROM hotels AS h
            JOIN tour_documents AS d
              ON d.entity_type = 'hotel' AND d.entity_id = h.hotel_id
             AND d.chunk_type = 'summary' AND d.chunk_index = 0
            WHERE h.city = %s
              AND (%s IS NULL OR h.price <= %s)
              AND d.embedding IS NOT NULL
            ORDER BY d.embedding <=> %s::vector, h.price, h.rating DESC
            LIMIT %s
            """,
            (query_vector, region, max_price, max_price, query_vector, count),
        )
        if items:
            return {
                "items": items,
                "count": len(items),
                "requested_count": count,
                "filters": {"region": region, "max_price": max_price, "query": query},
                "sort": "similarity_desc_then_price_asc",
                "search_mode": "vector",
                "source": "local-pgvector",
            }

    items = fetch_all(
        f"""
        SELECT {HOTEL_COLUMNS}
        FROM hotels AS h
        WHERE h.city = %s AND (%s IS NULL OR h.price <= %s)
        ORDER BY h.price, h.rating DESC, h.review_count DESC, h.name
        LIMIT %s
        """,
        (region, max_price, max_price, count),
    )
    return {
        "items": items,
        "count": len(items),
        "requested_count": count,
        "filters": {"region": region, "max_price": max_price, "query": query or None},
        "sort": "price_asc",
        "search_mode": "structured_fallback" if query else "structured",
        "source": "local-pgvector",
    }


@mcp.tool()
def search_tourist_attractions(
    region: str,
    count: int = 5,
    query: str = "",
) -> dict:
    """지역으로 대한민국 관광지를 검색하며 count 기본값은 5입니다."""
    region = required_text(region, "region")
    query = query.strip()
    validate_options(None, count)
    columns = "a.id, a.city, a.area, a.name, a.address, a.description, a.precautions"

    if query:
        query_vector = vector_literal(create_embedding(query))
        items = fetch_all(
            f"""
            SELECT {columns}, 1 - (d.embedding <=> %s::vector) AS similarity
            FROM tourist_attractions AS a
            JOIN tour_documents AS d
              ON d.entity_type = 'attraction' AND d.entity_id = a.id::text
             AND d.chunk_type = 'summary' AND d.chunk_index = 0
            WHERE a.city = %s AND d.embedding IS NOT NULL
            ORDER BY d.embedding <=> %s::vector, a.area, a.name
            LIMIT %s
            """,
            (query_vector, region, query_vector, count),
        )
        if items:
            return {
                "items": items,
                "count": len(items),
                "requested_count": count,
                "filters": {"region": region, "query": query},
                "search_mode": "vector",
                "source": "local-pgvector",
            }

    items = fetch_all(
        f"""
        SELECT {columns}
        FROM tourist_attractions AS a
        WHERE a.city = %s
        ORDER BY a.area, a.name
        LIMIT %s
        """,
        (region, count),
    )
    return {
        "items": items,
        "count": len(items),
        "requested_count": count,
        "filters": {"region": region, "query": query or None},
        "search_mode": "structured_fallback" if query else "structured",
        "source": "local-pgvector",
    }


@mcp.tool()
def recommend_hotels_near_attraction(
    attraction_name: str,
    max_price: int | None = None,
    count: int = 5,
    query: str = "",
) -> dict:
    """관광지와 같은 구역·도시의 호텔을 우선순위에 따라 추천합니다."""
    attraction_name = required_text(attraction_name, "attraction_name")
    query = query.strip()
    validate_options(max_price, count)

    attractions = fetch_all(
        """
        SELECT id, city, area, name, address, description
        FROM tourist_attractions
        WHERE name = %s
        ORDER BY city, area
        """,
        (attraction_name,),
    )
    if not attractions:
        attractions = fetch_all(
            """
            SELECT id, city, area, name, address, description
            FROM tourist_attractions
            WHERE name ILIKE %s
            ORDER BY city, area, name
            LIMIT 10
            """,
            (f"%{attraction_name}%",),
        )
    if not attractions:
        return {
            "status": "not_found",
            "attraction": None,
            "hotels": [],
            "count": 0,
            "message": "해당 관광지를 찾을 수 없습니다.",
            "source": "local-pgvector",
        }
    if len(attractions) > 1:
        return {
            "status": "ambiguous_attraction",
            "candidates": attractions,
            "message": "관광지 이름이 여러 건과 일치합니다. 정확한 이름을 입력해 주세요.",
            "source": "local-pgvector",
        }

    attraction = attractions[0]
    similarity_select = ""
    document_join = ""
    similarity_order = ""
    if query:
        query_vector = vector_literal(create_embedding(query))
        similarity_select = ", 1 - (d.embedding <=> %s::vector) AS similarity"
        document_join = """
        JOIN tour_documents AS d
          ON d.entity_type = 'hotel' AND d.entity_id = h.hotel_id
         AND d.chunk_type = 'summary' AND d.chunk_index = 0
         AND d.embedding IS NOT NULL
        """
        similarity_order = "d.embedding <=> %s::vector,"

    if query:
        sql_params = (
            attraction["area"], query_vector, attraction["city"], max_price,
            max_price, attraction["area"], query_vector, count,
        )
    else:
        sql_params = (
            attraction["area"], attraction["city"], max_price, max_price,
            attraction["area"], count,
        )
    hotels = fetch_all(
        f"""
        SELECT {HOTEL_COLUMNS},
               CASE WHEN h.district = %s THEN 'same_area' ELSE 'same_city' END
                   AS proximity_level
               {similarity_select}
        FROM hotels AS h
        {document_join}
        WHERE h.city = %s AND (%s IS NULL OR h.price <= %s)
        ORDER BY CASE WHEN h.district = %s THEN 0 ELSE 1 END,
                 {similarity_order} h.price, h.rating DESC, h.review_count DESC
        LIMIT %s
        """,
        sql_params,
    )
    return {
        "status": "ok",
        "attraction": attraction,
        "hotels": hotels,
        "count": len(hotels),
        "requested_count": count,
        "filters": {"max_price": max_price, "query": query or None},
        "matching_basis": "same_area_then_same_city",
        "search_mode": "vector" if query else "structured",
        "distance_notice": "현재 추천은 행정구역 기준이며 실제 거리 계산 결과가 아닙니다.",
        "source": "local-pgvector",
    }


@mcp.resource("tour://guide/korea")
def korea_tour_guide() -> str:
    """대한민국 호텔 및 관광지 검색 서비스 안내입니다."""
    return (
        "대한민국 내 호텔과 관광지 명소 정보를 제공합니다. "
        "가격을 지정하지 않은 호텔 검색은 낮은 가격순으로 최대 5개를 반환합니다. "
        "자연어 조건은 pgvector 유사도 검색에 사용합니다. "
        "관광지 주변 호텔은 현재 동일 행정구역과 도시를 기준으로 추천합니다."
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
