from fastapi import FastAPI, HTTPException
from poke_jacobiano import (
    Movimiento,
    PokemonOscuridad,
    PokemonRayo,
    Combate
)

app = FastAPI()

pokemons = {}
combate_actual = None

# Movimientos predefinidos
MOVIMIENTOS = {
    "Oscuridad": [
        Movimiento("Examen_dificil", 30, PokemonOscuridad),
        Movimiento("Juicio_final", 25, PokemonOscuridad),
        Movimiento("Conocimiento_profundo", 20, PokemonOscuridad),
        Movimiento("Frikada", 35, PokemonOscuridad),
    ],
    "Rayo": [
        Movimiento("Disparo_rapido", 28, PokemonRayo),
        Movimiento("Ocho_manos", 22, PokemonRayo),
        Movimiento("Finta", 32, PokemonRayo),
        Movimiento("Cafe_explosivo", 50, PokemonRayo),
    ]
}


@app.post("/pokemon")
def crear_pokemon(data: dict):
    nombre = data["nombre"]
    tipo = data["tipo"]

    if nombre in pokemons:
        raise HTTPException(400, "El Pokémon ya existe")

    if tipo == "Oscuridad":
        pokemon = PokemonOscuridad(
            nombre, 50, 150, 35, 40, 90, MOVIMIENTOS["Oscuridad"]
        )
    elif tipo == "Rayo":
        pokemon = PokemonRayo(
            nombre, 18, 140, 25, 17, 180, MOVIMIENTOS["Rayo"]
        )
    else:
        raise HTTPException(400, "Tipo no válido")

    pokemons[nombre] = pokemon
    return {"mensaje": f"{nombre} creado correctamente"}


@app.get("/pokemon")
def listar_pokemon():
    return list(pokemons.keys())


@app.post("/combate/iniciar")
def iniciar_combate(data: dict):
    global combate_actual

    p1 = pokemons.get(data["pokemon1"])
    p2 = pokemons.get(data["pokemon2"])

    if not p1 or not p2:
        raise HTTPException(404, "Pokemon no encontrado")

    combate_actual = Combate(p1, p2)
    return {"mensaje": "Combate iniciado"}


@app.post("/combate/turno")
def ejecutar_turno():
    if combate_actual is None:
        raise HTTPException(400, "No hay combate activo")

    return combate_actual.turno()
