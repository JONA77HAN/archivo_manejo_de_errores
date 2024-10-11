def crear_lista():
    animales = []
    cantidad_ingresados = 0
    
    while cantidad_ingresados < 5:
        print('Ingresa un animal a nuestra lista:')
        animal = input()  # Recibimos la entrada del usuario

        if any(char.isdigit() for char in animal):  # Comprobamos si hay números
            print('No ingreses números, por favor.')
            continue  # Volvemos a iniciar el ciclo sin contar este intento

        animales.append(animal)  # Agregamos el animal a la lista
        cantidad_ingresados += 1  # Aumentamos el contador
        print('Te faltan ingresar', (5 - cantidad_ingresados), 'animales.')
    
    return animales

# Llamamos a la función y mostramos la lista
animales = crear_lista()
print('La lista de animales quedó así:', animales)
