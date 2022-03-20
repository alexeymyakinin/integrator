from __future__ import annotations

from typing import TypedDict, Callable

from app.types import EntityType, Direction


class Handler(TypedDict):
    entity: EntityType
    direction: Direction
    processor: Callable[..., ...]
