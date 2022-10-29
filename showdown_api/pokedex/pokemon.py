import json
from showdown_api import showdown_request

def get_pokemon(pokemon_name: str) -> json:
    return {pokemon_name: 'test'} 