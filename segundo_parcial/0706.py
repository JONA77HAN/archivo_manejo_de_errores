import pandas as pd

# Creación de un DataFrame
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 45, 35, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao']
}
df = pd.DataFrame(datos)
print(df)