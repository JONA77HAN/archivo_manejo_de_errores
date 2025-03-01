import random

# Programa para elegir un inicial de Kanto
def elegir_inicial():
    print("¡Bienvenido al mundo Pokémon!")
    print("Puedes elegir uno de los tres iniciales de Kanto:")
    print("1. Bulbasaur 🌱 (Planta/Veneno)")
    print("2. Charmander 🔥 (Fuego)")
    print("3. Squirtle 🌊 (Agua)")
    
    while True:
        try:
            eleccion = int(input("Ingresa el número de tu elección (1, 2 o 3): "))
            if eleccion == 1:
                print("¡Has elegido a Bulbasaur! 🌱")
                return "Bulbasaur", ["Latigazo", "Polvo Veneno"]
            elif eleccion == 2:
                print("¡Has elegido a Charmander! 🔥")
                return "Charmander", ["Ascuas", "Arañazo"]
            elif eleccion == 3:
                print("¡Has elegido a Squirtle! 🌊")
                return "Squirtle", ["Pistola Agua", "Placaje"]
            else:
                print("Por favor, ingresa un número válido (1, 2 o 3).")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

# Función para evolucionar al Pokémon inicial
def evolucionar_inicial(pokemon):
    evoluciones = {
        "Bulbasaur": "Ivysaur 🌱",
        "Ivysaur": "Venusaur 🌱",
        "Charmander": "Charmeleon 🔥",
        "Charmeleon": "Charizard 🔥",
        "Squirtle": "Wartortle 🌊",
        "Wartortle": "Blastoise 🌊"
    }
    if pokemon in evoluciones:
        evolucionado = evoluciones[pokemon]
        print(f"¡Tu {pokemon} ha evolucionado a {evolucionado}!")
        return evolucionado
    else:
        print("Este Pokémon no puede evolucionar.")
        return pokemon

# Función para encontrar un Pokémon aleatorio
def encontrar_pokemon():
    pokemon_encontrados = {
        "Rattata 🐭": "¿Qué tipo de Pokémon es Rattata? (a) Normal (b) Agua (c) Fuego",
        "Cubone 🦴": "¿Qué lleva Cubone en la cabeza? (a) Un casco (b) Un hueso (c) Una roca",
        "Snorlax 😴": "¿Qué le gusta hacer a Snorlax? (a) Dormir (b) Correr (c) Luchar",
        "Ditto 🟣": "¿Qué habilidad especial tiene Ditto? (a) Transformarse (b) Curarse (c) Volar",
        "Eevee 🦊": "¿Cuántas evoluciones tiene Eevee en la primera generación? (a) Tres (b) Cuatro (c) Dos",
    }
    encontrado = random.choice(list(pokemon_encontrados.keys()))
    print(f"¡Has encontrado un {encontrado}!")
    return encontrado, pokemon_encontrados[encontrado]

# Función para intentar atrapar un Pokémon
def intentar_atrapar(pokemon, pregunta):
    print("¿Quieres intentar atraparlo? (sí/no)")
    respuesta = input().strip().lower()
    if respuesta in ["sí", "si"]:
        print(pregunta)
        respuesta_correcta = {
            "Rattata 🐭": "a",
            "Cubone 🦴": "b",
            "Snorlax 😴": "a",
            "Ditto 🟣": "a",
            "Eevee 🦊": "a",
            "Moltres 🔥": "a",
            "Articuno ❄️": "a",
            "Zapdos ⚡": "c"
        }
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta[pokemon]:
            print(f"¡Felicidades! Has atrapado a {pokemon}.")
            return pokemon
        else:
            print(f"¡Oh no! {pokemon} escapó.")
    else:
        print(f"Dejaste que {pokemon} se fuera.")
    return None

# Función para enfrentar al entrenador Pablo
def enfrentar_entrenador(pokemon_inicial, movimientos, atrapado):
    print("\nTe enfrentas al entrenador Pablo. ¡Prepárate!")
    print("El equipo de Pablo es: Metapod 🐛 y Raichu ⚡.")

    # Primera batalla contra Metapod
    print("Pablo envía a Metapod 🐛.")
    print(f"Tienes a {pokemon_inicial}. Movimientos disponibles: {movimientos}")
    movimiento = input("Elige un movimiento para atacar: ").strip()
    
    if movimiento == movimientos[0]:  # Movimiento correcto para vencer a Metapod
        print("¡Es muy efectivo! Metapod no puede seguir peleando.")
    else:
        print("No fue muy efectivo. Metapod sigue en pie.")
        return pokemon_inicial  # Termina la batalla si no derrotas a Metapod

    # Segunda batalla contra Raichu
    print("Pablo envía a Raichu ⚡.")
    if atrapado:
        print(f"Usas a {atrapado} para la batalla.")
    else:
        print(f"Sigues con {pokemon_inicial}.")
    
    print("Para ganar, responde la siguiente pregunta:")
    print("¿Cuál es el tipo de Raichu? (a) Eléctrico (b) Normal (c) Agua")
    respuesta = input("Tu respuesta: ").strip().lower()
    if respuesta == "a":
        print("¡Correcto! Has vencido a Raichu y ganado la batalla contra Pablo.")
    else:
        print("¡Incorrecto! Raichu te derrotó. Intenta de nuevo más tarde.")
        return pokemon_inicial

    # Evolución obligatoria después de la batalla
    print("\nDespués de la batalla, tu Pokémon inicial evoluciona de nuevo.")
    pokemon_inicial = evolucionar_inicial(pokemon_inicial)
    return pokemon_inicial

# Función para enfrentar a Gastly y Mew
def enfrentar_gastly_y_mew(pokemon_inicial, movimientos):
    print("\nMientras exploras, te encuentras con Gastly 👻 y Mew ✨.")
    print("Gastly te ataca. ¡Prepárate para la batalla!")

    # Batalla contra Gastly
    print(f"Tienes a {pokemon_inicial}. Movimientos disponibles: {movimientos}")
    movimiento = input("Elige un movimiento para atacar a Gastly: ").strip()
    if movimiento == movimientos[1]:  # Movimiento diferente al usado contra Metapod
        print("¡Es muy efectivo! Gastly ha sido derrotado.")
        print("Has capturado a Gastly 👻, pero Mew ✨ escapa volando.")
    else:
        print("No fue muy efectivo. Gastly te derrota y ambos Pokémon escapan.")

# Función para encontrar aves legendarias
def encontrar_aves_legendarias():
    aves_legendarias = {
        "Moltres 🔥": "¿Cuál es el tipo principal de Moltres? (a) Agua (b) Fuego (c) Planta",
        "Articuno ❄️": "¿Cual es el poder de Articuno? (a) Conjelar (b) Intimidar (c) Quemar",
        "Zapdos ⚡": "¿En qué tipo de clima aparece Zapdos? (a) Nevadas (b) Lluvias (c) Tormentas"
    }
    encontrado = random.choice(list(aves_legendarias.keys()))
    print(f"¡Has encontrado a {encontrado}!")
    return encontrado, aves_legendarias[encontrado]

# Ejecutar el programa
def main():
    inicial, movimientos = elegir_inicial()
    atrapado = None
    
    if inicial:
        while True:
            evolucionar = input("¿Quieres evolucionar a tu Pokémon? (sí/no): ").strip().lower()
            if evolucionar in ["sí", "si"]:
                inicial = evolucionar_inicial(inicial)
                break
            elif evolucionar == "no":
                print(f"¡Disfruta tu aventura con {inicial}!")
                break
            else:
                print("Por favor, responde con 'sí' o 'no'.")
        
        print("\nMientras exploras, te encuentras con algo interesante...")
        pokemon, pregunta = encontrar_pokemon()
        atrapado = intentar_atrapar(pokemon, pregunta)
    
    # Batalla contra Pablo
    inicial = enfrentar_entrenador(inicial, movimientos, atrapado)

    # Encuentro con Gastly y Mew
    enfrentar_gastly_y_mew(inicial, movimientos)

    # Encuentro con aves legendarias
    print("\nMás adelante, te encuentras con un trío legendario.")
    ave, pregunta_ave = encontrar_aves_legendarias()
    intentar_atrapar(ave, pregunta_ave)

# Iniciar el programa principal
if __name__ == "__main__":
    main()