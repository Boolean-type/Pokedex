import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

from Metodo_Jacobiano.poke_jacobiano import (
    PokemonOscuridad,
    PokemonRayo,
    Combate,
    Pokemon,      # ← necesario para from_dict
    MOVIMIENTOS
)

app = FastAPI()

pokemons: dict[str, Pokemon] = {}
combate_actual: Combate | None = None


# ==================== MODELOS PYDANTIC ====================
class PokemonCreate(BaseModel):
    nombre: str
    tipo: Literal["Oscuridad", "Rayo"]


class IniciarCombate(BaseModel):
    pokemon1: str
    pokemon2: str


# ==================== PERSISTENCIA ====================
def save_pokemon_to_json(pokemon: Pokemon):
    """Guarda/actualiza el Pokémon en pokemons.json"""
    data = pokemon.to_dict()
    file_path = "pokemons.json"

    # Leer datos existentes
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            pokemons_data = json.load(f)
    else:
        pokemons_data = {}

    pokemons_data[data["nombre"]] = data

    # Guardar
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(pokemons_data, f, indent=4, ensure_ascii=False)


@app.on_event("startup")
async def load_pokemons():
    """Carga todos los Pokémon guardados al iniciar la API"""
    global pokemons
    file_path = "pokemons.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for nombre, p_data in data.items():
            pokemons[nombre] = Pokemon.from_dict(p_data)


# ==================== ENDPOINTS ====================
@app.post("/pokemon")
def crear_pokemon(pokemon: PokemonCreate):
    if pokemon.nombre in pokemons:
        raise HTTPException(status_code=400, detail="El Pokémon ya existe")

    if pokemon.tipo == "Oscuridad":
        p = PokemonOscuridad(
            pokemon.nombre, 50, 150, 35, 40, 90, MOVIMIENTOS["Oscuridad"]
        )
    else:  # Rayo
        p = PokemonRayo(
            pokemon.nombre, 18, 140, 25, 17, 180, MOVIMIENTOS["Rayo"]
        )

    pokemons[pokemon.nombre] = p
    save_pokemon_to_json(p)                     # ← Aquí se guarda en JSON

    return {"mensaje": f"{pokemon.nombre} creado correctamente"}


@app.get("/pokemon")
def listar_pokemon():
    return list(pokemons.keys())


@app.post("/combate/iniciar")
def iniciar_combate(data: IniciarCombate):
    global combate_actual

    p1 = pokemons.get(data.pokemon1)
    p2 = pokemons.get(data.pokemon2)

    if not p1 or not p2:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")

    combate_actual = Combate(p1, p2)
    return {"mensaje": "Combate iniciado"}


@app.post("/combate/turno")
def ejecutar_turno():
    if combate_actual is None:
        raise HTTPException(status_code=400, detail="No hay combate activo")

    return combate_actual.turno()