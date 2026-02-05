**GET /api/pokemons:** Recupera una lista de todos los Pokémon disponibles en el sistema, incluyendo sus stats básicos (nombre, nivel, vida, fuerza, defensa, velocidad y movimientos asociados). No requiere parámetros. Respuesta en JSON, por ejemplo:JSON

```
[  
  {  
    "nombre": "Jacobo",  
    "nivel": 50,  
    "vida": 150,  
    "fuerza": 35,  
    "defensa": 40,  
    "velocidad": 90,  
    "tipo": "Oscuridad",  
    "movimientos": ["Examen_dificil", "Juicio_final", "Conocimiento_profundo", "Frikada"]  
  },  
  {  
    "nombre": "Jahn",  
    "nivel": 18,  
    "vida": 140,  
    "fuerza": 25,  
    "defensa": 17,  
    "velocidad": 180,  
    "tipo": "Rayo",  
    "movimientos": ["Disparo_rapido", "Ocho_manos", "Finta", "Cafe_explosivo"]  
  }  
]  

```

**GET /api/pokemons/{nombre}:** Recupera los detalles específicos de un Pokémon por su nombre (por ejemplo, /api/pokemons/Jacobo). Respuesta en JSON con los mismos campos que en la lista anterior. Si no existe, devuelve 404.
GET /api/movimientos: Recupera una lista de todos los movimientos disponibles, agrupados por tipo de Pokémon. Respuesta en JSON, por ejemplo:

**GET /api/movimientos:** Recupera una lista de todos los movimientos disponibles, agrupados por tipo de Pokémon. Respuesta en JSON, por ejemplo:

```
{  
  "Oscuridad": [  
    {"nombre": "Examen_dificil", "daño_base": 30},  
    {"nombre": "Juicio_final", "daño_base": 25},  
    ...  
  ],  
  "Rayo": [  
    {"nombre": "Disparo_rapido", "daño_base": 28},  
    ...  
  ]  
}  
```

**POST /api/crearpokemon:** Crea un nuevo Pokémon. Requiere un body en JSON con los campos: nombre, nivel, vida, fuerza, defensa, velocidad, tipo, y una lista de nombres de movimientos. Ejemplo de body:

```
{  
  "nombre": "Jacobo",  
  "nivel": 30,  
  "vida": 120,  
  "fuerza": 30,  
  "defensa": 25,  
  "velocidad": 100,  
  "tipo": "Oscuridad",  
  "movimientos": ["Examen_dificil", "Juicio_final"]  
}  

```
Valida que los movimientos sean compatibles con el tipo (usando la lógica existente en el constructor de Pokemon). Respuesta: 201 con el Pokémon creado en JSON, o 400 si hay errores de validación. Útil para agregar Pokémon personalizados y probar la creación.

**POST /api/combate:** Inicia una nueva batalla. Requiere un body en JSON especificando los nombres de los dos Pokémon (por ejemplo, {"pokemon1": "Jacobo", "pokemon2": "Jahn"}). Ejecuta la batalla completa pero en lugar de imprimir, devuelve un log en JSON como un array de turnos:

```
{  
  "ganador": "Jacobo",  
  "turnos": [  
    {"turno": 1, "accion": "Jacobo usa Examen_dificil contra Jahn", "daño": 13, "vida_restante_jahn": 127},  
    {"turno": 1, "accion": "Jahn usa Disparo_rapido contra Jacobo", "daño": 8, "vida_restante_jacobo": 142},  
    ...  
  ]  
}  

```

Si un Pokémon no existe, devuelve 404.

