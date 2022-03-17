from integrator.synchronizator.context import Context


async def items_in(context: Context):
    yield {"id": 1, "name": "name"}


async def orders_in(context: Context):
    yield {"id": 1, "name": "name"}
