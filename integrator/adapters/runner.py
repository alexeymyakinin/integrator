from __future__ import annotations

from integrator.adapters.adapter import Adapter


class Runner:
    def __init__(self, adapter: Adapter):
        self._adapter = adapter

    async def run(self):
        for handler in self._adapter.get_handlers():
            await handler()
