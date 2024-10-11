def crear_lista():
    animales = []
    cantidad_ingresados = 0
    while not cantidad_ingresados>10:
        try:
            print('Ingresa un animal a nuestra lista \n')
            animal = str(input())
            animales.append(animal)
            cantidad_ingresados += 1
            print('te faltan ingresar ',(cantidad_ingresados - 10), ' animales' )
        except:
            print('no ingreses numeros!')
    return animales
            
animales = crear_lista()
print('La lista de animales quedó asi ', animales)