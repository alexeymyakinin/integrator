from app.sync.adapter.adapter import Adapter


class Runner:
    def __init__(self, adapter: Adapter):
        self._adapter = adapter

    async def run(self):
        for handler in self._adapter.get_handlers():
            async for resp in handler(self._adapter):
                print(resp)
