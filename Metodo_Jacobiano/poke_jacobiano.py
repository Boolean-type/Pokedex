import random


class Movimiento:
    def __init__(self, nombre, daño_base, tipo_pokemon):
        self._nombre = nombre
        self._daño_base = daño_base
        self._tipo_pokemon = tipo_pokemon  # CLASE, no instancia

    def get_nombre(self):
        return self._nombre

    def get_tipo_pokemon(self):
        return self._tipo_pokemon

    def calcular_daño(self, defensa_objetivo):
        daño = self._daño_base + (self._daño_base * 0.10)
        daño -= defensa_objetivo
        return max(0, int(daño))

class Pokemon:
    def __init__(self, nombre, nivel, vida, fuerza, defensa, velocidad, movimientos):
        self._nombre = nombre
        self._nivel = nivel
        self._vida = vida
        self._fuerza = fuerza
        self._defensa = defensa
        self._velocidad = velocidad

        # Validar movimientos
        for movimiento in movimientos:
            if movimiento.get_tipo_pokemon() is not self.__class__:
                raise ValueError(
                    f"El movimiento {movimiento.get_nombre()} no es válido para {self.__class__.__name__}"
                )

        self._movimientos = movimientos


    def get_nombre(self):
        return self._nombre

    def get_vida(self):
        return self._vida

    def get_defensa(self):
        return self._defensa

    def get_velocidad(self):
        return self._velocidad

   
    def set_vida(self, vida):
        self._vida = max(0, vida)

    # -------- COMBATE --------
    def ejecutar_movimiento(self, otro_pokemon):
        movimiento = random.choice(self._movimientos)
        print(f"{self._nombre} usa {movimiento.get_nombre()} contra {otro_pokemon.get_nombre()}")
        daño = movimiento.calcular_daño(otro_pokemon.get_defensa())
        otro_pokemon.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.set_vida(self._vida - daño)
        print(f"{self._nombre} recibe {daño} de daño. Vida restante: {self._vida}")

class PokemonOscuridad(Pokemon):
    pass


class PokemonRayo(Pokemon):
    pass
