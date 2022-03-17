from databases import Database
from fastapi import APIRouter, Depends
from sqlalchemy import func

from app.models.models import ItemBase, ListItem, CreateItem
from app.schemas.postgres import item as item_schema
from app.web.dependencies import get_db, get_paging

router = APIRouter(
    tags=['item'],
    prefix='/context/items',
)


@router.get('/', response_model=ListItem)
async def items_paging(paging: dict = Depends(get_paging), database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            limit = paging['limit']
            total = await connection.fetch_val(func.count(item_schema.c.id).select())
            items = await connection.fetch_all(item_schema
                                               .select()
                                               .limit(paging['limit'])
                                               .offset(paging['offset']))
            return ListItem(**{'limit': limit, 'total': total, 'items': items})


@router.get('/{id}', response_model=ItemBase)
async def items_get_id(item_id: int, database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            return await connection.fetch_all(item_schema
                                              .select()
                                              .where(item_schema.c.id == item_id))


@router.post('/', response_model=ItemBase)
async def items_create(item: CreateItem, database: Database = Depends(get_db)):
    async with database.connection() as connection:
        async with connection.transaction():
            return await connection.fetch_one(item_schema
                                              .insert(item.dict()))
