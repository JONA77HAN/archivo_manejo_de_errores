# Diccionario de Pokémon con sus tipos
pokemons = {
    'pikachu': ['Electric'],
    'bulbasaur': ['Grass', 'Poison'],
    'charmander': ['Fire'],
    'squirtle': ['Water'],
    'eevee': ['Normal'],
    'jigglypuff': ['Fairy', 'Normal'],
    'meowth': ['Normal'],
    'snorlax': ['Normal'],
    'mewtwo': ['Psychic'],
    'charizard': ['Fire', 'Flying'],
    # Añade más Pokémon aquí si lo deseas
}

# Función para obtener la información de un Pokémon
def obtener_info_pokemon(nombre):
    # Convertimos el nombre del Pokémon a minúsculas para hacer la búsqueda sin importar mayúsculas/minúsculas
    nombre = nombre.lower()

    # Comprobamos si el Pokémon está en el diccionario
    if nombre in pokemons:
        tipos = pokemons[nombre]
        print(f"Información de {nombre.capitalize()}:")
        print(f"Tipos: {', '.join(tipos)}")
    else:
        print("Pokémon no encontrado. Por favor, verifica el nombre e intenta de nuevo.")

# Menú principal
def menu():
    print("Bienvenido al sistema de información de Pokémon!")
    while True:
        print("\nSelecciona una opción:")
        print("1. Obtener información de un Pokémon específico")
        print("2. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == '1':
            pokemon_nombre = input("Introduce el nombre del Pokémon: ")
            obtener_info_pokemon(pokemon_nombre)
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Inicia el programa
if __name__ == "__main__":
    menu()
