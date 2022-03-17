from __future__ import annotations

from typing import Tuple

from integrator.synchronizator.adapter.adapter import Adapter
from integrator.synchronizator.types import Entity, RunnerException, HandlerEntity, HandlerDirection


class Runner:
    @staticmethod
    async def run(adapter: Adapter):
        for handler in adapter.get_handlers():
            handler_func = handler['processor']
            handler_entity = handler['entity']
            handler_direction = handler['direction']
            async for resp in handler_func():
                match resp:
                    case tuple():
                        await Runner._process_entity(handler_entity, handler_direction, resp)
                    case _:
                        raise RunnerException()

    @staticmethod
    async def _process_entity(entity: HandlerEntity, direction: HandlerDirection, resp: Tuple[Entity, Entity]):
        pass
