from __future__ import annotations

from typing import Iterable

from functional import seq

from integrator.synchronizator.types import Handler, AdapterSettings


class Adapter:
    def __init__(self):
        self._name = str()
        self._version = str()
        self._base_url = str()
        self._handlers = set()
        self._settings = dict()

    def with_name(self, name: str) -> Adapter:
        self._name = name
        return self

    def with_version(self, version: str) -> Adapter:
        self._version = version
        return self

    def with_base_url(self, base_url: str) -> Adapter:
        self._base_url = base_url
        return self

    def with_handler(self, handler: Handler) -> Adapter:
        self._handlers.add(handler)
        return self

    def with_settings(self, settings: AdapterSettings) -> Adapter:
        self._settings.update(settings)
        return self

    def get_handlers(self) -> Iterable[Handler]:
        return seq(self._handlers)
