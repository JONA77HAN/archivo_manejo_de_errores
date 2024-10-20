archivo = open('C:/Users/Usuario/Desktop/YONI/PC/google_colab/personas.csv')
personas_crudo = archivo.readlines()
archivo.close()

#print(personas_crudo)

def transformar(persona):
    persona = persona.strip('\n')
    persona = persona.split(';')
    return persona

personas = list(map(transformar, personas_crudo))

sumas_edades = 0
for [nombre, edad] in personas:
    sumas_edades += int(edad)

print('el promedio de edad es:', sumas_edades/len(personas))
