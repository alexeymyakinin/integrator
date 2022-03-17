from typing import Dict

from httpx import AsyncClient


class BaseAPI:
    def __init__(self, base_url: str):
        self._base_url = base_url

    async def _make_request(self, method: str, url: str, as_json: bool = True, **kwargs) -> None:
        async with AsyncClient() as client:
            request = await client.request(method, self._base_url + url, **kwargs)
            response = await client.send(request, **kwargs)

            if as_json:
                response = await response.json()

            return response


class ClientAPI(BaseAPI):
    def __init__(self, base_url: str, name: str):
        super().__init__(base_url)
        self._name = name

    async def get(self, id_: str):
        pass

    async def list(self, params: Dict):
        pass

    async def create(self, body: Dict):
        pass

    async def update(self, body: Dict):
        pass

    async def delete(self, params: Dict):
        pass
