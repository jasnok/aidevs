"""Tour MCP Server에서 사용하는 PostgreSQL 공통 접근 함수."""

import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row


# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# load_dotenv(PROJECT_ROOT / ".env")

load_dotenv()

def database_url() -> str:
    url = os.getenv("DATABASE_URL", "").strip()
    if not url:
        raise RuntimeError("DATABASE_URL 환경변수가 필요합니다.")
    return url


@contextmanager
def get_connection() -> Iterator[psycopg.Connection]:
    """dict 행을 반환하는 DB 연결을 열고 사용 후 닫습니다."""
    with psycopg.connect(database_url(), row_factory=dict_row) as connection:
        yield connection


def fetch_all(query: str, params: tuple[Any, ...] = ()) -> list[dict]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()


def fetch_one(query: str, params: tuple[Any, ...] = ()) -> dict | None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

