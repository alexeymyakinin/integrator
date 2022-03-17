from databases import Database

from app.config import DATABASE_URL

DB = Database(DATABASE_URL)


def get_db() -> Database:
    return DB


def get_paging(limit: int | None = 100, offset: int | None = 0) -> dict[str, int]:
    return {
        'limit': limit,
        'offset': offset
    }
