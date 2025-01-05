archivo = open('C:/Users/Usuario/Desktop/YONI/PC/archivos/salando.txt')
contenido = archivo.readlines()
archivo.close()

for linea in contenido:
    print(linea)
