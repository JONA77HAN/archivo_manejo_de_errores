#armar una lista q incluya 3 animales

animales = []
cantidad_ingresados = 0
while cantidad_ingresados != 3:
    print('ingresa un animal para la lista: \n')
    animal = input()
    animales.append(animal)
    cantidad_ingresados += 1
    print('Ingresaste',animal, 'te restan por agregar', 3 - cantidad_ingresados, 'animales')
print('la lista quedo armada asi\n', animales)    
    
for animal in animales:
    print(animal)

       