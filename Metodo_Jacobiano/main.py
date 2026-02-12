from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .pokemon_persistence import load_pokemons, save_pokemon
from .poke_jacobiano import (
    PokemonOscuridad,
    PokemonRayo,
    Combate,
    Pokemon,
    MOVIMIENTOS,
    TIPOS_PERMITIDOS,
)


app = FastAPI()

pokemons: dict[str, Pokemon] = {}
combate_actual: Combate | None = None


class PokemonCreate(BaseModel):
    nombre: str
    tipo: str          # ← ahora es str + validamos con lista


class IniciarCombate(BaseModel):
    pokemon1: str
    pokemon2: str

# ==================== ENDPOINTS ====================
@app.post("/pokemon")
def crear_pokemon(pokemon: PokemonCreate):
    if pokemon.nombre in pokemons:
        raise HTTPException(status_code=400, detail="El Pokémon ya existe")

    if pokemon.tipo not in TIPOS_PERMITIDOS:
        raise HTTPException(status_code=400, detail="Tipo no válido")

    if pokemon.tipo == "Oscuridad":
        p = PokemonOscuridad(
            pokemon.nombre, 50, 150, 35, 40, 90, MOVIMIENTOS["Oscuridad"]
        )
    else:  # Rayo
        p = PokemonRayo(
            pokemon.nombre, 18, 140, 25, 17, 180, MOVIMIENTOS["Rayo"]
        )

 
    save_pokemon(p)                     # ← guarda en JSON

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