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

    def ejecutar_movimiento(self, otro_pokemon):
        movimiento = random.choice(self._movimientos)
        daño = movimiento.calcular_daño(otro_pokemon.get_defensa())
        otro_pokemon.recibir_daño(daño)

        return {
            "atacante": self._nombre,
            "movimiento": movimiento.get_nombre(),
            "daño": daño,
            "vida_objetivo": otro_pokemon.get_vida()
        }

    def recibir_daño(self, daño):
        self.set_vida(self._vida - daño)


class PokemonOscuridad(Pokemon):
    pass


class PokemonRayo(Pokemon):
    pass


class Combate:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def turno(self):
        if self.p1.get_velocidad() >= self.p2.get_velocidad():
            atacante, defensor = self.p1, self.p2
        else:
            atacante, defensor = self.p2, self.p1

        resultado = atacante.ejecutar_movimiento(defensor)

        return {
            "resultado_turno": resultado,
            "vidas": {
                self.p1.get_nombre(): self.p1.get_vida(),
                self.p2.get_nombre(): self.p2.get_vida()
            }
        }
