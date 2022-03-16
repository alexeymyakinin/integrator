from databases import Database
from fastapi import APIRouter, Depends
from sqlalchemy import func

from integrator.models.models import ListOrder, OrderBase, CreateOrder
from integrator.schemas.schema import order as order_schema
from integrator.web.dependencies import get_db, get_paging

router = APIRouter(
    tags=['order'],
    prefix='/api/order',
)


@router.get('/', response_model=ListOrder)
async def orders_paging(paging: dict = Depends(get_paging), database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            limit = paging['limit']
            total = await connection.fetch_val(func.count(order_schema.c.id).select())
            orders = await connection.fetch_all(order_schema
                                                .select()
                                                .limit(paging['limit'])
                                                .offset(paging['offset']))
            return ListOrder(**{'limit': limit, 'total': total, 'orders': orders})


@router.get('/{id}', response_model=OrderBase)
async def orders_get_id(order_id: int, database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            return await connection.fetch_all(order_schema
                                              .select()
                                              .where(order_schema.c.id == order_id))


@router.post('/', response_model=OrderBase)
async def orders_create(order: CreateOrder, database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            return await connection.fetch_one(order_schema
                                              .insert(order.dict()))
