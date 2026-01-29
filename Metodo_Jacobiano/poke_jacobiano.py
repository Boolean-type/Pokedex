import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, fuerza, defensa, velocidad, movimientos):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.movimientos = movimientos  # lista de objetos Movimiento

    def ejecutar_movimiento(self, otro_pokemon):
        movimiento = random.choice(self.movimientos)

        print(f"{self.nombre} usa {movimiento.nombre} contra {otro_pokemon.nombre}")

        daño = movimiento.calcular_daño(otro_pokemon.defensa)
        otro_pokemon.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibe {daño} de daño. Vida restante: {self.vida}")


class Movimiento:
    def __init__(self, nombre, daño_base):
        self.nombre = nombre
        self.daño_base = daño_base

    def calcular_daño(self, defensa_objetivo):
        """
        daño = daño_base + 10% del daño_base - defensa del objetivo
        """
        daño = self.daño_base + (self.daño_base * 0.10) - defensa_objetivo

        if daño < 0:
            daño = 0

        return int(daño)
