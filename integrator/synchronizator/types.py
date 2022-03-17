from __future__ import annotations

import enum
from typing import Dict, Callable, AsyncGenerator, TypedDict, Tuple

from integrator.synchronizator.context import Context

Entity = Dict

AdapterSettings = Dict
HandlerProcessorFunc = Callable[[Context], AsyncGenerator[Tuple[Entity, Entity]]]


class Handler(TypedDict):
    entity: HandlerEntity
    direction: HandlerDirection
    processor: HandlerProcessorFunc


class HandlerEntity(enum.Enum):
    items = enum.auto()
    stock = enum.auto()
    orders = enum.auto()


class HandlerDirection(enum.Enum):
    IN = enum.auto()
    OUT = enum.auto()


class RunnerException(Exception):
    pass
