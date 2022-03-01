from itertools import count


c = count(start=5, step=0.1)
# esse count retorna um iterador que conta indefinidamente, 
# a não ser que eu informe os parametros
for x in c:
    print(round(x, 2))
    if x >= 10:
        break
x = count()
l = ['lui', 'lie', 'lei']
zz = list(zip(x, l))
print(zz)