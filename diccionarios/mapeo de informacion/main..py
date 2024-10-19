productos = {}

cgo = int(input('ingrese un codigo, 0 para terminar '))
while cgo != 0:
    if cgo not in productos:
        desc = input('descripcion de %d ' %cgo )
        unidad = input('unidad de medida de %s ' %desc)
        precio = float (input('Precio unitario de %s ' %desc))
        productos[cgo] = (desc, unidad, precio)
    cgo = int(input('ingrese codigo, 0 para terminar '))
for cgo in productos:
    print(cgo, *productos[cgo]) 
total = 0
cgo = int(input('que lleva? 0 para salir '))
while cgo not in productos and cgo != 0:
    cgo = int(input('que lleva? 0 para salir '))
while cgo != 0:
    cant = float (input('cantidad de %s '%(productos[cgo])))
    total += cant*productos[cgo] [2]
    cgo = int (input('¿qué lleva? 0 para salir'))
    while cgo not in productos and cgo != 0:
        cgo = int(input('¿qué lleva? 0 para salir '))    
print('Debe abonar: $%.2f'%total, sep='')        
