def mes30(m):
    de30dias=(4,6,9,11)
    return m in de30dias  #va a devolver True o False
#PPal
meses=[1,5,6,2,7]
de30=list(filter(mes30,meses))
print(de30)
