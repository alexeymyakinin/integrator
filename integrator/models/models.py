from typing import List

from pydantic import create_model, BaseModel
from sqlalchemy import Table

from integrator.schemas.schema import user, item, stock, order, order_line, location, vendor


def convert_to_pydantic(definition: Table, *exclude: str):
    return create_model(str(definition.name),
                        **{
                            str(name): prop.type.python_type
                            for name, prop in definition.columns.items()
                            if name not in exclude
                        })


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


class ListItem(PagingResponse):
    items: List[ItemBase]
