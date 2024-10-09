archivo = open('carpeta/personas.csv')
personas_crudo = archivo.readlines()
archivo.close()

#print(personas_crudo)
def transformar(persona):
    persona = persona.strip('\n')
    persona = persona.split(';')
    return persona

personas = map(transformar, personas_crudo)
print(list(personas))
