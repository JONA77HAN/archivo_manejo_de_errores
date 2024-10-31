def vocFin(n):
    voc='aeiouáéíóú'
    return n[-1].lower()in voc
#PPal
nom=input('Nombre finalizado en vocal: ')
while not vocFin(nom) or not nom.isalpha():
    nom=input('Nombre finalizado en vocal: ')