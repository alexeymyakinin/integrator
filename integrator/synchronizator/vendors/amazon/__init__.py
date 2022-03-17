from integrator.synchronizator.adapter.adapter import Adapter
from integrator.synchronizator.types import HandlerEntity, HandlerDirection
from integrator.synchronizator.vendors.amazon.handlers import items_in, orders_in


def get_adapter() -> Adapter:
    return (Adapter()
            .with_name('Amazon')
            .with_version('0.0.1')
            .with_settings(dict(url='index/'))
            .with_handler(dict(entity=HandlerEntity.items,
                               direction=HandlerDirection.IN,
                               processor=items_in))
            .with_handler(dict(entity=HandlerEntity.orders,
                               direction=HandlerDirection.IN,
                               processor=orders_in)))
