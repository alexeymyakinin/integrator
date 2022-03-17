from __future__ import annotations

from typing import Set, Dict, Any, AsyncGenerator

from functional import seq

from sync.adapter.handler import Handler
from sync.context.client import ClientAPI
from sync.context.vendor import VendorAPI
from sync.types import Setting


class AdapterBuilder:
    def __init__(self):
        self._config: Dict[str, Any] = dict()
        self._config['handlers'] = set()
        self._config['settings'] = set()

    def build(self):
        return Adapter(**self._config)

    def with_name(self, name: str) -> AdapterBuilder:
        self._config['name'] = name
        return self

    def with_version(self, version: str) -> AdapterBuilder:
        self._config['version'] = version
        return self

    def with_handler(self, handler: Handler) -> AdapterBuilder:
        self._config['handlers'].add(handler)
        return self

    def with_setting(self, setting: Setting) -> AdapterBuilder:
        self._config['settings'].add(setting)
        return self

    def with_client_base_url(self, url: str) -> AdapterBuilder:
        self._config['client_base_url'] = url
        return self

    def with_vendor_base_url(self, url: str) -> AdapterBuilder:
        self._config['vendor_base_ulr'] = url
        return self


class Adapter:
    def __init__(self,
                 *,
                 name: str,
                 version: str,
                 handlers: Set[Handler],
                 settings: Set[Setting],
                 client_base_url: str,
                 vendor_base_url: str):
        self._name = name
        self._version = version
        self._handlers = handlers
        self._settings = settings
        self._client_api = ClientAPI(client_base_url)
        self._vendor_api = VendorAPI(vendor_base_url)

    @property
    def client_api(self):
        return self._client_api

    @property
    def vendor_api(self):
        return self._vendor_api

    def get_handlers(self) -> Set[AsyncGenerator]:
        return (seq(self._handlers)
                .map(lambda h: h['processor'])
                .map(lambda f: f(self))
                .set())
