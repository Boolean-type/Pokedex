import pytest
from poke_jacobiano import Pokemon, Movimiento


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
