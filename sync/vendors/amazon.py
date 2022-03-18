from sync.adapter.adapter import Adapter, AdapterBuilder
from sync.adapter.handler import Handler

from sync.types import Direction, EntityType


async def items_in(adapter: Adapter):
    yield {}


async def stock_in(adapter: Adapter):
    pass


def get_adapter():
    builder = (AdapterBuilder()
               .with_name('Amazon')
               .with_version('0.0.1')
               .with_setting({})
               .with_handler(Handler(entity=EntityType.items,
                                     direction=Direction.IN,
                                     processor=items_in)))
    return builder.build()
