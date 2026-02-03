from poke_jacobiano import (
    Movimiento,
    PokemonOscuridad,
    PokemonRayo
)

# Movimientos Oscuridad
Examen_dificil = Movimiento("Examen_dificil", 30, PokemonOscuridad)
Juicio_final = Movimiento("Juicio_final", 25, PokemonOscuridad)
Conocimiento_profundo = Movimiento("Conocimiento_profundo", 20, PokemonOscuridad)
Frikada = Movimiento("Frikada", 35, PokemonOscuridad)

# Movimientos Rayo
Disparo_rapido = Movimiento("Disparo_rapido", 28, PokemonRayo)
Ocho_manos = Movimiento("Ocho_manos", 22, PokemonRayo)
Finta = Movimiento("Finta", 32, PokemonRayo)
Cafe_explosivo = Movimiento("Cafe_explosivo", 50, PokemonRayo)


p1 = PokemonOscuridad(
    nombre="Jacobo",
    nivel=50,
    vida=150,
    fuerza=35,
    defensa=40,
    velocidad=90,
    movimientos=[Examen_dificil, Juicio_final, Conocimiento_profundo, Frikada]
)

p2 = PokemonRayo(
    nombre="Jahn",
    nivel=18,
    vida=140,
    fuerza=25,
    defensa=17,
    velocidad=180,
    movimientos=[Disparo_rapido, Ocho_manos, Finta, Cafe_explosivo]
)


if __name__ == "__main__":
    if p1.get_velocidad() >= p2.get_velocidad():
        atacante, defensor = p1, p2
    else:
        atacante, defensor = p2, p1

    turno = 1

    while p1.get_vida() > 0 and p2.get_vida() > 0:
        print(f"\n--- TURNO {turno} ---")

        atacante.ejecutar_movimiento(defensor)
        if defensor.get_vida() <= 0:
            break

        defensor.ejecutar_movimiento(atacante)
        turno += 1
