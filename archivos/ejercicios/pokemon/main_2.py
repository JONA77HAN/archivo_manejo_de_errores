from pprint import pprint

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

# Imprimir con pprint
pprint(pokemon_list)
