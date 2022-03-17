import asyncio

import uvicorn
import uvloop
from fastapi import FastAPI

from app.config import SERVICE_TEST
from app.routes import items
from app.schemas.postgres import metadata
from app.web.dependencies import get_db

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def create_app() -> FastAPI:
    app = FastAPI(
        debug=SERVICE_TEST,
    )
    app.include_router(items.router)

    @app.on_event('startup')
    async def on_startup():
        if app.debug:
            metadata.create_all()

        await get_db().connect()

    @app.on_event('shutdown')
    async def on_shutdown():
        if app.debug:
            metadata.drop_all()

        await get_db().disconnect()

    return app


if __name__ == '__main__':
    uvicorn.run(create_app())
