from typing import List

from pydantic import create_model, BaseModel
from sqlalchemy import Table

from integrator.schemas.schema import user, item, stock, order, order_line, location, vendor


def convert_to_pydantic(definition: Table, *exclude: str):
    name = str(definition.name).title()
    cols = {
        str(c_name): (c_prop.type.python_type, ... if c_prop.default is None and not c_prop.nullable else None)
        for c_name, c_prop in definition.c.items()
        if c_name not in exclude
    }

    return create_model(name, __base__=BaseModel, **cols)


UserBase = convert_to_pydantic(user)
ItemBase = convert_to_pydantic(item)
StockBase = convert_to_pydantic(stock)
OrderBase = convert_to_pydantic(order)
VendorBase = convert_to_pydantic(vendor)
LocationBase = convert_to_pydantic(location)
OrderLineBase = convert_to_pydantic(order_line)


class PagingResponse(BaseModel):
    total: int
    limit: int


class CreateRequest(BaseModel):
    class Config:
        fields = {'id': {'exclude': True}}


class ListItem(PagingResponse):
    items: List[ItemBase]


class ListOrder(PagingResponse):
    orders: List[OrderBase]


class CreateItem(ItemBase, CreateRequest):
    pass


class CreateOrder(OrderBase, CreateRequest):
    pass
