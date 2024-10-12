alumnos = []

def agregar_estudiante():
    nombre = input('Ingresa un nombre: ')
    dni = int(input('Ingresa su número de documento: '))
    edad = int(input('Ingresa tu edad: '))
    
    carrera = input('Ingresa la carrera que estás cursando: ')
    facultad = input('Ingresa en qué facultad estás cursando: ')
    
    estudiante = {
        'nombre': nombre,
        'dni': dni,
        'edad': edad,
        'estudios': {
            'carrera': carrera,
            'facultad': facultad
        }
    }
    alumnos.append(estudiante)

while True:
    print('1. Agregar Estudiante')
    print('2. Mostrar estudiantes')
    print('3. Salir')
    opcion = input('Ingresa una opción: ') 

    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        print(alumnos)
    elif opcion == '3':
        break   
    else:
        print('Ingresaste algo que no es una opción, por favor intenta de nuevo.')        


