"""호텔·관광지 검색 문장과 임베딩을 생성합니다."""

import hashlib
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# load_dotenv(PROJECT_ROOT / ".env")

load_dotenv()

EMBEDDING_MODEL = os.getenv("TOUR_EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_DIMENSIONS = int(os.getenv("TOUR_EMBEDDING_DIMENSIONS", "1536"))


def create_content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def build_hotel_content(hotel: dict) -> str:
    facilities = [
        label
        for field, label in (
            ("breakfast_included", "조식"),
            ("parking", "주차"),
            ("wifi", "와이파이"),
            ("pool", "수영장"),
        )
        if hotel.get(field)
    ]
    return "\n".join([
        f"호텔명: {hotel['name']}",
        f"지역: {hotel['city']} {hotel.get('district') or ''}".strip(),
        f"주소: {hotel.get('address') or ''}",
        f"가격: {hotel['price']}원",
        f"등급: {hotel.get('hotel_grade') or '미등록'}성급",
        f"객실 유형: {hotel.get('room_type') or '미등록'}",
        f"평점: {hotel.get('rating') or '미등록'}",
        f"편의시설: {', '.join(facilities) or '등록된 편의시설 없음'}",
        f"설명: {hotel.get('description') or ''}",
    ])


def build_attraction_content(attraction: dict) -> str:
    precautions = attraction.get("precautions") or []
    return "\n".join([
        f"관광지명: {attraction['name']}",
        f"지역: {attraction['city']} {attraction['area']}",
        f"주소: {attraction['address']}",
        f"설명: {attraction['description']}",
        f"주의사항: {' '.join(precautions)}",
    ])


def create_embedding(text: str) -> list[float]:
    normalized = text.strip()
    if not normalized:
        raise ValueError("임베딩할 텍스트는 비어 있을 수 없습니다.")

    response = OpenAI().embeddings.create(
        model=EMBEDDING_MODEL,
        input=normalized,
        dimensions=EMBEDDING_DIMENSIONS,
    )
    embedding = response.data[0].embedding
    if len(embedding) != EMBEDDING_DIMENSIONS:
        raise ValueError(
            "임베딩 차원이 설정과 일치하지 않습니다: "
            f"expected={EMBEDDING_DIMENSIONS}, actual={len(embedding)}"
        )
    return embedding


def vector_literal(embedding: list[float]) -> str:
    """pgvector가 입력받을 수 있는 '[1,2,...]' 문자열을 만듭니다."""
    return "[" + ",".join(str(value) for value in embedding) + "]"

