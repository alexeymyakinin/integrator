from __future__ import annotations

import enum
from collections import defaultdict
from functools import lru_cache, reduce
from typing import Any, List

from integrator.adapters.types import AdapterProcessorFunc


class AdapterDirection(enum.Enum):
    IN = enum.auto()
    OUT = enum.auto()


class Adapter:
    def __init__(self, vendor: str, version: str):
        self._vendor = vendor
        self._version = version

        self._handlers = defaultdict(dict)
        self._settings = defaultdict(dict)

    def with_handler(self,
                     entity_name: str,
                     direction: AdapterDirection,
                     processor: AdapterProcessorFunc) -> Adapter:
        self._handlers[direction][entity_name] = processor
        return self

    def with_setting(self, name: str, value: Any) -> Adapter:
        self._settings[name] = value
        return self

    @lru_cache
    def get_handlers(self) -> List:
        return reduce(lambda acc, val: acc | list(val.values()),
                      self._handlers,
                      initial=[])
