from poke_jacobiano import Pokemon, Movimiento

# Movimientos de tipo Oscuridad
Examen_dificil = Movimiento("Examen_dificil", 30, "Oscuridad")
Juicio_final = Movimiento("Juicio_final", 25, "Oscuridad")
Conocimiento_profundo = Movimiento("Conocimiento_profundo", 20, "Oscuridad")
Frikada = Movimiento("Frikada", 35, "Oscuridad")

# Movimientos de tipo Rayo
Disparo_rapido = Movimiento("Disparo_rapido", 28, "Rayo")
Ocho_manos = Movimiento("Ocho_manos", 22, "Rayo")
Finta = Movimiento("Finta", 32, "Rayo")
Cafe_explosivo = Movimiento("Cafe_explosivo", 50, "Rayo")

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

print("\n FIN DEL COMBATE ")
if p1.get_vida() <= 0:
    print(f"{p2.get_nombre()} gana")
else:
    print(f"{p1.get_nombre()} gana")
