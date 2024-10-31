#primer punto del parcial, vale 1 punto

"""
0106 – 1 Pto
¿Cuál de los siguientes códigos valida adecuadamente que ingrese un nombre finalizado con
vocal? Debe detectar el error y garantizar un dato válido
Ejs válidos: elena, Pedro, SANDRA
Ejs inválidos: javier, Inés, 9ema
Nota:
Un índice negativo (-i) aplicado a una secuencia hace referencia al elemento de la posición
len(secuencia)-i
Ej:
a=[1,23,56,7]
a[-2] -> 56
1
def vocFin(n):
voc='aeiouáéíóú'
return n[-1] not in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
while not vocFin(nom) or not nom.isalpha():
nom=input('Nombre finalizado en vocal: ')
1
2
def vocFin(n):
voc='aeiouáéíóú'
return n[len(n)-1] in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
if vocFin(nom):
if not nom.isalpha():
print('Ok')
else:
print('Ingreso Inválido, hasta pronto!')
else:
print('Ingreso Inválido, hasta pronto!')
2
3
def vocFin(n):
voc='aeiouáéíóú'
return n[-1].lower()in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
while not vocFin(nom) or not nom.isalpha():
nom=input('Nombre finalizado en vocal: ')
3
4
def vocFin(n):
voc='aeiouáéíóú'
return n[-1].upper() in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
if vocFin(nom) and nom.isalpha():
print('Ok')
else:
print('Ingreso Inválido, hasta pronto!')


DAME LA OPCION CORRECTA Y EXPLICAME DETALLADAMENTE EL PORQUE DE LA MISMA
*****************************************************************************************************
1)_

#Resolución:
def vocFin(n):
    voc='aeiouáéíóú'
    return n[-1] not in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
while not vocFin(nom) or not nom.isalpha():
    nom=input('Nombre finalizado en vocal: ')

ESTA NO ES CORRECTA YA Q LO Q BUSCA ES Q EL NOMBRE TERMINA EN CONSONANTE, NO EN VOCAL
COMO PIDE EL EJERCICIO


*****************************************************************************************************
2)_

def vocFin(n):
    voc = 'aeiouáéíóú'
    return n[len(n)-1] in voc

# Programa principal
nom = input('Nombre finalizado en vocal: ')
if vocFin(nom):
    if not nom.isalpha():
        print('Ok')
    else:
        print('Ingreso Inválido, hasta pronto!')
else:
    print('Ingreso Inválido, hasta pronto!')

#ESTA OPCION NO ES CORRECTA PORQUE EL CONDICIONAL IF NO PERMITE VOLVER A PREGUNTAR
#EN CASO DE QUE NO PONGAMOS CORRECTAMENTE EL NOMBRE DESDE UN PRINCIPIO

********************************************************************************************************
4)_   #LUEGO VAMOS CON LA 3 QUE ES LA CORRECTA

def vocFin(n):
    voc = 'aeiouáéíóú'
    return n[-1].upper() in voc

# Programa principal
nom = input('Nombre finalizado en vocal: ')
if vocFin(nom) and nom.isalpha():
    print('Ok')
else:
    print('Ingreso Inválido, hasta pronto!')

COMETE UN ERROR AL INICIO TRANSFORMANDO LA LETRRA A MAYUS LO Q NOS DARA ERROR
TAMBIEN LA ESTRUCTURA CON IF NO NOS SIRVE YA Q NO NOS PERMITE RE INTENTOS

*******************************************************************************************************
    
    """
#AHORA VAMOS CON LA OPCION TRES, LA CORRECTA
# 3)_

def vocFin(n):
    voc = 'aeiouáéíóú'
    return n[-1].lower() in voc

# Programa principal
nom = input('Nombre finalizado en vocal: ')
while not vocFin(nom) or not nom.isalpha():
    nom = input('Nombre finalizado en vocal: ')







