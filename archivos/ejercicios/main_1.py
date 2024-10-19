"""
Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la
respuesta dada por el usuario en el archivo.
Por ejemplo,s e tiene el archivo pregunta.txt que originalmente tiene:
¿Cómo estás hoy?
Y el usuario de la respuesta: “¡Bien, porque me comí una hamburguesa!”
Entonces el archivo debería quedar de la forma:
¿Cómo estás hoy?
¡Bien, porque me comí una hamburguesa!

"""

archivo = open('C:/Users/Usuario/Desktop/YONI/PC/archivos/ejercicios/ejercicio_1.txt', 'w')
print('Hola, ¿cómo estas?')
respuesta = input()
contenido = archivo.write(respuesta)
archivo.close()
