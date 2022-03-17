from __future__ import annotations

from enum import Enum, auto
from typing import Dict, Any


class EntityType(Enum):
    items = auto()
    stock = auto()
    orders = auto()


class Direction(Enum):
    IN = auto()
    OUT = auto()


Entity = Dict[str, Any]
Setting = Dict[str, Any]
