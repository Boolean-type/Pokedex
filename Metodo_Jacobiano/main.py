# Script que me va a ejecutar la logica siguiente:

# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vvida <= 0 pierde

from poke_jacobiano import Pokemon,Movimiento

# Movimientos
Examen_dificil = Movimiento("Examen_dificil", 30)
Juicio_final = Movimiento("Juicio_final", 25)
Conocimiento_profundo = Movimiento("Conocimiento_profundo", 20)
Frikada = Movimiento("Frikada", 35)

Disparo_rapido = Movimiento("Disparo_rapido", 28)
Ocho_manos = Movimiento("Ocho_manos", 22)
Finta = Movimiento("Finta", 32)
Cafe_explosivo = Movimiento("Cafe_explosivo", 50)


# ---------- ESCENARIO ----------
p1 = Pokemon(
    nombre="Jacobo",
    tipo="Oscuridad",
    nivel=50,
    vida=150,
    fuerza=35,
    defensa=40,
    velocidad=90,
    movimientos=[Examen_dificil, Juicio_final, Conocimiento_profundo, Frikada]
)

p2 = Pokemon(
    nombre="Jahn",
    tipo="Rayo",
    nivel=18,
    vida=140,
    fuerza=25,
    defensa=17,
    velocidad=180,
    movimientos=[Disparo_rapido, Ocho_manos, Finta, Cafe_explosivo]
)


# Quién empieza
if p1.velocidad >= p2.velocidad:
    atacante, defensor = p1, p2
else:
    atacante, defensor = p2, p1

turno = 1

while p1.vida > 0 and p2.vida > 0:
    print(f"\n--- TURNO {turno} ---")

    atacante.ejecutar_movimiento(defensor)
    if defensor.vida <= 0:
        break

    defensor.ejecutar_movimiento(atacante)
    turno += 1

print("\n FIN DEL COMBATE ")
if p1.vida <= 0:
    print(f"{p2.nombre} gana")
else:
    print(f"{p1.nombre} gana")
