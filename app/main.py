import asyncio
import sys

import uvicorn
from fastapi import FastAPI

from app.config import SERVICE_TEST
from app.routes import items, sync
from app.sync.vendors import vendors

if sys.platform != 'win32':
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def create_app() -> FastAPI:
    app = FastAPI(
        debug=SERVICE_TEST,
    )
    app.include_router(items.router)
    app.include_router(sync.create_routes(vendors))

    # @app.on_event('startup')
    # async def on_startup():
    #     if app.debug:
    #         metadata.create_all()
    #
    #     await get_db().connect()
    #
    # @app.on_event('shutdown')
    # async def on_shutdown():
    #     if app.debug:
    #         metadata.drop_all()
    #
    #     await get_db().disconnect()

    print([r.path for r in app.routes])
    return app


if __name__ == '__main__':
    uvicorn.run(create_app())
