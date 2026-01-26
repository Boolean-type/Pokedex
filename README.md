# Pokedex
Katas de Jacobo

## ENTIDADES (clases)

### 1.- Pokémon
Representa a una especie de Pokémon (no a uno individual capturado).

**Atributos:**
id
nombre
tipo
altura
peso
descripción
habilidades
estadisticas_base (PS, ataque, defensa, etc.)

**Responsabilidad:**

Contener la información “enciclopédica” del Pokémon.

### 2.- Tipo

**Atributos:**

Nombre (Fuego, Agua, Planta…)
debilidades
resistencias

**Responsabilidad:**
Definir cómo interactúa con otros tipos.

### 3.- Habilidad

**Atributos:**
nombre
descripción
efecto (puede ser solo texto o lógica más compleja)

**Responsabilidad:**
Describir efectos pasivos o especiales.

### 4.- Movimiento
**Atributos:**
nombre
tipo
potencia
precision
categoria (físico / especial / estado)
efecto_secundario

**Responsabilidad:**
Definir cómo ataca un Pokémon.

### 5. Evolución

**Atributos:**
pokemon_origen
pokemon_destino
condicion (nivel, objeto, intercambio, felicidad…)

**Responsabilidad:**
Definir cuándo y cómo evoluciona un Pokémon.
