'''
zip - unindo iteraveis
zip_longest - itertools
'''

from itertools import zip_longest, count
index = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA',]
cidades_estados = zip(index, estados, cidades)
print(next(cidades_estados))
for i, c, e in cidades_estados:
    print(i, c, e)

# com a função zip eu crio uma tupla

