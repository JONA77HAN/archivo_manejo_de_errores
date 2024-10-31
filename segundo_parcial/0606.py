"""Para averiguar la posición o número de orden de un alumno en una lista de nombres. ¿Cuál
función impide que aborte la ejecución del mismo si se ingresa el nombre
Sanz, Ignacio ?
def donde(…):
-
-
-
alumnos=['Andreoli, Julieta','Vargas, Ulises','Fiquet, Paulo']
alum=input('Nombre: ')
pos=donde(alumnos,alum)
print(alum,pos)
Nota:
El método index() devuelve la posición de un elemento en una lista. Si el elemento no está,
se aborta la ejecución del programa
Ej:
[1,2,3].index(3) -> 2
"""

def donde(alumnos,alum):
    try:
        indice=alumnos.index(alum)
        cartel='está en la posición '+str(indice+1)
    except:
        cartel='NO ESTÁ EN LA LISTA'
        return cartel


alumnos=['Andreoli, Julieta','Vargas, Ulises','Fiquet, Paulo']
alum=input('Nombre: ')
pos=donde(alumnos,alum)
print(alum,pos)