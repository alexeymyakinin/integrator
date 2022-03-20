from typing import Dict

from fastapi import APIRouter
from starlette.background import BackgroundTasks
from starlette.responses import Response

from app.sync.adapter.adapter import Adapter
from app.sync.runner.runner import Runner


def create_routes(vendors: Dict[str, Adapter]) -> APIRouter:
    router = APIRouter(prefix='/api/sync/vendors')
    for name, adapter in vendors.items():
        @router.post(f'/{name}/run')
        async def run_vendor_sync(background_tasks: BackgroundTasks):
            runner = Runner(adapter)
            background_tasks.add_task(runner.run)
            return Response(status_code=200)
    return router
