from databases import Database
from fastapi import APIRouter, Depends
from sqlalchemy import func

from integrator.models.models import ItemBase, ListItem
from integrator.schemas import schema
from integrator.web.dependencies import get_db, get_paging

router = APIRouter(
    tags=['item'],
    prefix='/api/items',
)


@router.get('/')
async def items_paging(paging: dict = Depends(get_paging), database: Database = Depends(get_db)) -> ListItem:
    async with database.connection() as connection:
        async with connection.transaction():
            limit = paging['limit']
            total = await connection.fetch_val(func.count(schema.item.c.id).select())
            items = await connection.fetch_all(schema.item
                                               .select()
                                               .limit(paging['limit'])
                                               .offset(paging['offset']))
            return ListItem(**{'limit': limit, 'total': total, 'items': items})


@router.get('/{id}')
async def items_get_id(id_: int, database: Database = Depends(get_db)) -> ItemBase:
    async with database.connection() as connection:
        async with connection.transaction():
            return await connection.fetch_all(schema.item
                                              .select()
                                              .where(schema.item.c.id == id_))
