from requests import get, Response
from typing import Callable, Optional


class ShowdownRequest:
    request_uri:str
    execute: Callable

    def __init__(self, uri:str, request: Callable[[Optional[dict]], Response]):
        self.request_uri = uri
        self.execute = request

    @staticmethod
    def showdown_request_factory(path: str, subdomain: str = None) -> Response:
        query_uri = f"https://{f'{subdomain}.' if subdomain else ''}pokemonshowdown.com{path}.json"

        def get_request(options: dict = None) -> Response:
            return get(query_uri, params=options)

        return ShowdownRequest(query_uri, get_request)
