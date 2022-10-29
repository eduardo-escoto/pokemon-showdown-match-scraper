from showdown_api.showdown_request import ShowdownRequest

json_file_paths = {"pokemon": "pokemon.json"}


def save_pokemon_json():
    request = ShowdownRequest.showdown_request_factory(
        "/data/pokedex", subdomain="play"
    )

    save_json(request.execute().json(), json_file_paths["pokemon"])


save_pokemon_json()
