archivo = open('C:/Users/Usuario/Desktop/YONI/PC/archivos/indio.txt')
contenido = archivo.readlines()
archivo.close()

contador = 0

for linea in contenido:
    if 'su' in linea:
        contador += 1
print('la palabra "su" aparece', contador, 'veces')        
