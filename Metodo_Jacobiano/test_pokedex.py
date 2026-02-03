import pytest
from poke_jacobiano import Pokemon, Movimiento
import main

def test_movimiento_mismo_tipo_y_en_lista():
    movimiento = Movimiento("Ataque Oscuro", 30, "Oscuridad")

    pokemon = Pokemon(
        nombre="Testmon",
        tipo="Oscuridad",
        nivel=10,
        vida=100,
        fuerza=20,
        defensa=15,
        velocidad=30,
        movimientos=[movimiento]
    )

    assert movimiento in pokemon.get_movimientos()
    assert movimiento.get_tipo() == pokemon.get_tipo()


def test_movimiento_tipo_incorrecto_lanza_excepcion():
    movimiento = Movimiento("Rayo Mortal", 40, "Rayo")

    with pytest.raises(ValueError):
        Pokemon(
            nombre="Testmon",
            tipo="Oscuridad",
            nivel=10,
            vida=100,
            fuerza=20,
            defensa=15,
            velocidad=30,
            movimientos=[movimiento]
        )


def test_todos_los_pokemon_son_instancias_de_pokemon():
    from poke_jacobiano import Pokemon

    for pokemon in main.POKEMONS:
        assert isinstance(pokemon, Pokemon)


def test_todos_los_pokemon_tienen_cuatro_movimientos():
    for pokemon in main.POKEMONS:
        assert len(pokemon.get_movimientos()) == 4