import random

class Movimiento:
    def __init__(self, nombre: str, daño_base: int, tipo_pokemon):
        self._nombre = nombre
        self._daño_base = daño_base
        self._tipo_pokemon = tipo_pokemon  # CLASE, no instancia

    def get_nombre(self) -> str:
        return self._nombre

    def get_tipo_pokemon(self):
        return self._tipo_pokemon

    def calcular_daño(self, defensa_objetivo: int) -> int:
        daño = self._daño_base + (self._daño_base * 0.10)
        daño -= defensa_objetivo
        return max(0, int(daño))


class Pokemon:
    def __init__(self, nombre: str, nivel: int, vida: int, fuerza: int, defensa: int, velocidad: int, movimientos: list):
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

    def get_nombre(self) -> str:
        return self._nombre

    def get_vida(self) -> int:
        return self._vida

    def get_defensa(self) -> int:
        return self._defensa

    def get_velocidad(self) -> int:
        return self._velocidad

    def set_vida(self, vida: int):
        self._vida = max(0, vida)

    def ejecutar_movimiento(self, otro_pokemon: "Pokemon") -> dict:
        movimiento = random.choice(self._movimientos)
        daño = movimiento.calcular_daño(otro_pokemon.get_defensa())
        otro_pokemon.recibir_daño(daño)

        return {
            "atacante": self._nombre,
            "movimiento": movimiento.get_nombre(),
            "daño": daño,
            "vida_objetivo": otro_pokemon.get_vida()
        }

    def recibir_daño(self, daño: int):
        self.set_vida(self._vida - daño)

    # ==================== SERIALIZACIÓN ====================
    def to_dict(self) -> dict:
        tipo_str = "Oscuridad" if isinstance(self, PokemonOscuridad) else "Rayo"
        return {
            "nombre": self._nombre,
            "tipo": tipo_str,
            "nivel": self._nivel,
            "vida": self._vida,
            "fuerza": self._fuerza,
            "defensa": self._defensa,
            "velocidad": self._velocidad,
            "movimientos": [m.get_nombre() for m in self._movimientos]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pokemon":
        nombre = data["nombre"]
        nivel = data["nivel"]
        vida = data["vida"]
        fuerza = data["fuerza"]
        defensa = data["defensa"]
        velocidad = data["velocidad"]
        tipo = data["tipo"]

        movimientos = MOVIMIENTOS[tipo]

        if tipo == "Oscuridad":
            return PokemonOscuridad(nombre, nivel, vida, fuerza, defensa, velocidad, movimientos)
        elif tipo == "Rayo":
            return PokemonRayo(nombre, nivel, vida, fuerza, defensa, velocidad, movimientos)
        else:
            raise ValueError(f"Tipo desconocido: {tipo}")


class PokemonOscuridad(Pokemon):
    pass


class PokemonRayo(Pokemon):
    pass


class Combate:
    def __init__(self, p1: Pokemon, p2: Pokemon):
        self.p1 = p1
        self.p2 = p2

    def turno(self) -> dict:
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


# Movimientos predefinidos (ahora aquí para poder usarlos en from_dict)
MOVIMIENTOS = {
    "Oscuridad": [
        Movimiento("Examen_dificil", 30, PokemonOscuridad),
        Movimiento("Juicio_final", 25, PokemonOscuridad),
        Movimiento("Conocimiento_profundo", 20, PokemonOscuridad),
        Movimiento("Frikada", 35, PokemonOscuridad),
    ],
    "Rayo": [
        Movimiento("Disparo_rapido", 28, PokemonRayo),
        Movimiento("Ocho_manos", 22, PokemonRayo),
        Movimiento("Finta", 32, PokemonRayo),
        Movimiento("Cafe_explosivo", 50, PokemonRayo),
    ]
}
TIPOS_PERMITIDOS = ["Oscuridad", "Rayo"]