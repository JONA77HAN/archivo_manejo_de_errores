import random

def generar_palabras():
    palabras = ["caca", "amburgesa", "estrella de mar", "casa millonaria", "montaña pribada", "rio pribado", "bosque de mieda literal mente", "nube", "viento", "fuego", 
                "inbocador de truenos", "mini-roca", "una perspna que te putea", "culo comestibles", "brisa helada", "tierra gratis", "oxigeno", "nube solida", "relámpago", "lluvia todo un mes"]
    seleccionadas = random.sample(palabras, 10)
    return seleccionadas

if __name__ == "__main__":
    palabras = generar_palabras()
    print(" 1 ".join(palabras))
    print(" 2 ".join(palabras))
    print(" 3 ".join(palabras))
    print(" 4 ".join(palabras))
    print(" 5 ".join(palabras))

 
