# Lista para almacenar los estudiantes
estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante():
    nombre = input('Ingrese el nombre del estudiante: ')
    dni = input('Ingrese el DNI del estudiante: ')
    edad = int(input('Ingrese la edad del estudiante: '))
    
    año = int(input('Ingrese el año del curso: '))
    división = input('Ingrese la división del curso: ')
    orientación = input('Ingrese la orientación del curso: ')
    
    estudiante = {
        'nombre': nombre,
        'DNI': dni,
        'edad': edad,
        'curso': {
            'año': año,
            'división': división,
            'orientación': orientación
        }
    }
    
    estudiantes.append(estudiante)
    print('Estudiante agregado con éxito.\n')

# Función para mostrar el estudiante con mayor edad
def mostrar_mayor_edad():
    if estudiantes:
        estudiante_mayor_edad = max(estudiantes, key=lambda x: x['edad'])
        print('Estudiante con mayor edad:')
        print(estudiante_mayor_edad)
    else:
        print('No hay estudiantes en la lista.')

# Menú principal
while True:
    print('1. Agregar estudiante')
    print('2. Mostrar estudiante con mayor edad')
    print('3. Salir')
    opción = input('Seleccione una opción: ')
    
    if opción == '1':
        agregar_estudiante()
    elif opción == '2':
        mostrar_mayor_edad()
    elif opción == '3':
        break
    else:
        print('Opción inválida. Intente nuevamente.\n')
