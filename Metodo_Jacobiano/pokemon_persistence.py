import json
import os
from typing import Dict

from .poke_jacobiano import Pokemon

FILE_PATH = "pokemons.json"


def load_pokemons() -> Dict[str, Pokemon]:
    """Carga todos los Pokémon desde pokemons.json"""
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data: dict = json.load(f)

    pokemons: Dict[str, Pokemon] = {}
    for nombre, p_data in data.items():
        pokemons[nombre] = Pokemon.from_dict(p_data)

    return pokemons


def save_pokemon(pokemon: Pokemon) -> None:
    """Guarda o actualiza un Pokémon en el archivo JSON"""
    data = pokemon.to_dict()

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            pokemons_data: dict = json.load(f)
    else:
        pokemons_data: dict = {}

    pokemons_data[data["nombre"]] = data

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(pokemons_data, f, indent=4, ensure_ascii=False)