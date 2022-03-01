"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +, min, max
range

"""
"""

#uma lista pode receber qulquer tipo de item
x = [1, 1.0, 'a', True]

#indice:    0    1       2    3   4
lista =   ['a', 'bike', 'c', 'd', 1]
#indice n:  5    4       3    2   1

#as listas também suportam fatiamento
print(lista[0::2])
#mostrando a lista invertida
print(lista[::-1])

"""
"""
#usando a função .extend() eu consigo colocar o conteudo de uma lista dentro de outra
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
print(l2)
"""
"""
#usando a função .append() eu adiciono um novo item ao final da lista
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.append('a')
print(l1)
print(l2)
"""
"""
#usando a função .insert() eu afasto os itens da lista e incluo um novo no meio deles
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.insert(1, 'a')
print(l1)
print(l2)
"""
"""
#usando .pop eu deleto o ultimo item da lista
lista = [1, 2, 3, 4]
print(lista)
lista.pop()
print(lista)
"""
"""
#usando del() eu excluo itens especificos na lista
lista = [1, 2, 3, 4]
print(lista)
lista.insert(0, 'bro')
print(lista)
del(lista[0])
print(lista)
"""
"""
#usando max() e min() eu consigo achar os maiores e menores valores da lista
lista = [1, 2, 3, 4, 5, 6]
print(max(lista))
print(min(lista))
"""
"""
#testando tipos
l2 = ['string', True, 10, -20.5]
for itens in l2:
    print('O tipo de {} é {}'.format(itens, type(itens)))
"""
secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra: ')
    if len(letra)> 1:
        print('Informe apenas 1 letra')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print('Letra correta! {} Existe na palavra'.format(letra))
    else:
        print('A letra {} não existe na palavra!'.format(letra))
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario = secreto_temporario + '-'
    if secreto_temporario == secreto:
        print('Você acertou a palavra!')
        break
    else:
        print('A palavra, até o momento: {}'.format(secreto_temporario))



