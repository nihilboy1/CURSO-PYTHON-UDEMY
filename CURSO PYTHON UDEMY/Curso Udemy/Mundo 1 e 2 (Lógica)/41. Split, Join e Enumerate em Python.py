"""
split, join e enumerate em python
"""
"""
# a função split divide a string baseada no argumento informado nos parenteses
x = 'Eu gosto de mamão'
x2 = x.split(' ')
print(x2)
"""
"""
#o join junta lista em strings normais, utilizando o argumento que estiver entre os parenteses
list = ['oi,', 'eu', 'gosto', 'de', 'você!']
print(list)
jlist = ' '.join(list)
print(jlist.strip().capitalize())
"""
"""
#usando o enumerate, eu informo dois valores pra o meu for ''rodar'', e o primeiro deles vai servir de indice
#a variavel que recebe o enumerate, acompanha o contador numérico do laço
lista = ['oi,', 'eu', 'gosto', 'de', 'voce']
for indice, v1 in enumerate(lista):
    print(indice, v1.title())
"""
lista = [1, 2, 1, [3, 4]]
print(lista[2])
