import random

class Movimiento:
    def __init__(self, nombre, daño_base, tipo):
        self._nombre = nombre
        self._daño_base = daño_base
        self._tipo = tipo

    # -------- GETTERS --------
    def get_nombre(self):
        return self._nombre

    def get_daño_base(self):
        return self._daño_base

    def get_tipo(self):
        return self._tipo

    # -------- SETTERS --------
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_daño_base(self, daño_base):
        self._daño_base = daño_base

    def set_tipo(self, tipo):
        self._tipo = tipo

    def calcular_daño(self, defensa_objetivo):
        daño = self._daño_base + (self._daño_base * 0.10) - defensa_objetivo
        return max(0, int(daño))


class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, fuerza, defensa, velocidad, movimientos):
        self._nombre = nombre
        self._tipo = tipo
        self._nivel = nivel
        self._vida = vida
        self._fuerza = fuerza
        self._defensa = defensa
        self._velocidad = velocidad

        # Validación de movimientos
        for movimiento in movimientos:
            if movimiento.get_tipo() != tipo:
                raise ValueError(
                    f"El movimiento {movimiento.get_nombre()} no es del tipo {tipo}"
                )

        self._movimientos = movimientos

    # -------- GETTERS --------
    def get_nombre(self):
        return self._nombre

    def get_tipo(self):
        return self._tipo

    def get_vida(self):
        return self._vida

    def get_defensa(self):
        return self._defensa

    def get_velocidad(self):
        return self._velocidad

    def get_movimientos(self):
        return self._movimientos

    # -------- SETTERS --------
    def set_vida(self, vida):
        self._vida = max(0, vida)

    def set_movimientos(self, movimientos):
        for movimiento in movimientos:
            if movimiento.get_tipo() != self._tipo:
                raise ValueError(
                    f"El movimiento {movimiento.get_nombre()} no es del tipo {self._tipo}"
                )
        self._movimientos = movimientos

    # -------- MÉTODOS --------
    def ejecutar_movimiento(self, otro_pokemon):
        movimiento = random.choice(self._movimientos)
        print(f"{self._nombre} usa {movimiento.get_nombre()} contra {otro_pokemon.get_nombre()}")
        daño = movimiento.calcular_daño(otro_pokemon.get_defensa())
        otro_pokemon.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.set_vida(self._vida - daño)
        print(f"{self._nombre} recibe {daño} de daño. Vida restante: {self._vida}")
