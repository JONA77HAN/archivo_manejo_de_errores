def ingresar_los_10_numeros():
    numeros_ingresados = 0
    los_numeros = []
    
    while numeros_ingresados < 10:  # Cambiado a < 10 para ingresar 10 números
        try:
            print('Ingresa un múltiplo de 2:')
            numero = int(input())
            if numero % 2 == 0:  # Verificamos si el número es múltiplo de 2
                los_numeros.append(numero)  # Agregamos el número a la lista
                numeros_ingresados += 1  # Aumentamos el contador
            else:
                print('Ese número no es un múltiplo de 2. Inténtalo de nuevo.')
        except ValueError:  # Manejo de errores si la entrada no es un número
            print('Por favor, ingresa un número entero.')
    
    return los_numeros  # Devolvemos la lista de números

# Llamamos a la función y mostramos los números ingresados
numeros = ingresar_los_10_numeros()
print('Los números ingresados son:', numeros)
