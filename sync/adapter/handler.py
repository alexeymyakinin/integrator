from __future__ import annotations

from typing import TypedDict, Callable, Tuple, AsyncGenerator

from sync.types import EntityType, Direction, Entity


class Handler(TypedDict):
    entity: EntityType
    direction: Direction
    processor: Callable[[], AsyncGenerator[Tuple[Entity, Entity]]]
