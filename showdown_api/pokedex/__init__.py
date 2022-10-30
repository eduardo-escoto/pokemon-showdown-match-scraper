from showdown_api.showdown_request import ShowdownRequest
from showdown_api.utils.file_utils import *

api_data_path = "showdown_api_data"
pokedex_data_paths = {
    "pokemon": {"path": "/data/pokedex", "subdomain": "play", "file_ext": "json"},
    "moves": {"path": "/data/moves", "subdomain": "play", "file_ext": "json"},
    "items": {"path": "/data/items", "subdomain": "play", "file_ext": "js"},
}
json_file_paths = {
    "pokemon": "pokemon.json",
    "moves": "moves.json",
    "items": "items.json",
}
parse_funcs = {"js": save_js, "json": save_json}


def download_pokedex_data(key: str) -> None:
    file_type = pokedex_data_paths[key]["file_ext"]
    complete_path = f"{api_data_path}/{json_file_paths[key]}"

    def save_inner() -> None:
        request = ShowdownRequest.showdown_request_factory(**pokedex_data_paths[key])
        parse_funcs[file_type](
            request.execute().text, api_data_path, json_file_paths[key]
        )

    if (
        not file_exists(complete_path)
        or get_time_delta_now(complete_path) > 24 * 60 * 60
    ):
        save_inner()


for key in json_file_paths.keys():
    download_pokedex_data(key)
