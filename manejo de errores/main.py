def edad_usuario():
    es_correcta = False
    while (not es_correcta):
        try:
            print('ingrese su edad (solo numeros):')
            edad = int(input())
            es_correcta = True
        except:
            print('ingresa un numero entero por favor!')
    return edad 

edad = edad_usuario()
print('la edad ingresad del usuario es:', edad)
print(type(edad))