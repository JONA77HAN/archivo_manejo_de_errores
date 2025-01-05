"""

es_correcta = False
while (not es_correcta):
    try:
        print('hola, eres Lúcio?')
        nombre = str(input())
"""

def edad_usuario():
    es_correcta = False
    while (not es_correcta):
        try:
            print('ingrese su edad \n')
            edad = int(input())
            es_correcta = True
        except:
            print('ingresa un numero!!')
    return edad        