import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, fuerza, defensa, velocidad, movimientos):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida              # entre 100 y 300
        self.fuerza = fuerza          # máx 20
        self.defensa = defensa        # máx 18
        self.velocidad = velocidad    # máx 100
        self.movimientos = movimientos  # lista de 4 strings

    def ejecutar_movimiento(self, otro_pokemon):
        movimiento = random.choice(self.movimientos)
        print(f"{self.nombre} usa {movimiento} contra {otro_pokemon.nombre}")

        daño = self.fuerza - otro_pokemon.defensa
        if daño < 0:
            daño = 0

        otro_pokemon.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {daño} de daño. Vida restante: {self.vida}")
