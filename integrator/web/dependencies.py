from databases import Database

from integrator.config import DATABASE_URL

DB = Database(DATABASE_URL)


def get_paging(limit: int | None = 100, offset: int | None = 0) -> dict[str, int]:
    return {
        'limit': limit,
        'offset': offset
    }


def get_db() -> Database:
    return DB


