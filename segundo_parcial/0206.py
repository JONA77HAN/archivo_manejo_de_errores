def nomDia(d):
    dias={1:'domingo',2:'lunes',3:'martes',4:'miércoles',
    5:'jueves',6:'viernes',7:'sábado'}
    return dias[d]
#PPal
dias=[1,5,2,6,7]
nombres=list(map(nomDia,dias))
print(nombres)
