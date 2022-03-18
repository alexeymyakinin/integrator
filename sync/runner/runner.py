from typing import Iterable, AsyncGenerator


class Runner:
    def __init__(self, processors: Iterable[AsyncGenerator]):
        self.processors = processors

    async def run(self):
        async for resp in self.foo():
            pass
