import pandas as pd

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat',
'dog', 'dog'],
'age': [2.5, 3, 0.5, None, 5, 2, 4.5, None, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no',
'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index = labels )
#print(df.iloc[:5])   desde cual y hasta cual
#print(df.head(2))  #devuelve las columnas q le pedimos 
#print(df.loc[:,['age', 'visits']])  puedo elegir que columnas mostrar
print(df.loc[['a', 'c'],['age', 'visits']])  #puedo hacerlo por filas (primero) y tambien por columnas

#voy por el minuto 20:27 de este video
#print([df['visits'] == 2])

# NaN -->  quiere decir q algo es nulo # para preguntar si es nulo
print(df[df['visits'].isnull()])

#concatenando condiciones
#df[(df ['animal'] == 'cat') | (df ['age'] <3 ) ] #and -> &    or -> |     not -> coso de la ñ

print(df.loc[:, 'animal', 'age'])


