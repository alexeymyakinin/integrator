import uvicorn as uvicorn
from fastapi import FastAPI

from integrator.routes import items
from integrator.web.dependencies import get_db


def create_app() -> FastAPI:
    import uvloop
    import asyncio

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = FastAPI()
    app.debug = True
    app.include_router(items.router)

    @app.on_event('startup')
    async def on_startup():
        await get_db().connect()

    @app.on_event('shutdown')
    async def on_shutdown():
        await get_db().disconnect()

    return app


if __name__ == '__main__':
    uvicorn.run(create_app())
