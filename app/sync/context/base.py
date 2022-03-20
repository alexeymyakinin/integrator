from typing import Dict


class BaseAPI:
    def __init__(self,
                 base_url: str):
        self._base_url = base_url

    async def fetch(self,
                    url: str,
                    body: Dict,
                    query: Dict,
                    method: str = 'GET') -> Dict:
        pass
