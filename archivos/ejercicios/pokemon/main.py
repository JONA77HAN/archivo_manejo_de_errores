pokemon_list = []
with open('archivos/ejercicios/pokemon/pokemon_list.txt') as archivo:
    for linea in archivo:
        partes = linea.strip().split(', ')
        pokemon = {
            "nombre": partes[0].split('. ')[1],
            "tipo": partes[1],
            "altura": partes[2].split(': ')[1],
            "peso": partes[3].split(': ')[1]
        }
        pokemon_list.append(pokemon)

# Imprimir cada Pokémon en un formato más claro
for pokemon in pokemon_list:
    print(f"Nombre: {pokemon['nombre']}")
    print(f"  Tipo: {pokemon['tipo']}")
    print(f"  Altura: {pokemon['altura']}")
    print(f"  Peso: {pokemon['peso']}")
    print("-" * 30)

