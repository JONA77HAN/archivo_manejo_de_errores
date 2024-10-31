"""¿Qué contenido tendrá el archivo destacados.txt al finalizar la ejecución del programa
si el archivo deportistas.txt tiene el siguiente contenido?
Contenido de deportistas.txt:
lionel,messi,1
lucha,aymar,3
julián,álvarez,1
manu,ginobili,5
Programa a ejecutarse:"""

deportes={1:'Futbol',2:'Patín',3:'Hokey',4:'Tenis',5:'Basquet',6:'Ciclismo'}
arch=open('deportistas.txt','r')
lista=arch.readlines()
arch.close()
nom=[]
for dep in lista:
    d=dep.split(',')
    nom.append(d[0].upper()+' es de '+deportes[int(d[2])]+'\n')
    arch=open('destacados.txt','w')
    arch.writelines(nom)
    arch.close()

""""
Nota:
El método split() devuelve una lista con las partes de un texto tomando como separador
el argumento
Ej:
‘yo soy argentina’.split(‘ ‘) -> [‘yo’, ‘soy’, ‘argentina’]"""