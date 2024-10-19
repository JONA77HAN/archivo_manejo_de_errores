archivo = open('C:/Users/Usuario/Desktop/YONI/PC/archivos/salando.txt')
contenido = archivo.readlines()
print(contenido)
archivo.close()

print('o'*60)

for linea in contenido:
    print(linea)
