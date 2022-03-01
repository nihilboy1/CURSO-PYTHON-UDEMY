from random import randint


def sorteia(a):
    for c in range(1, 5):
        a.append(randint(1, 10))
    else:
        print(a)


def somapar(c):
    soma = 0
    for valor in c:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {c}, teremos a soma de {soma}')


numer = []
sorteia(numer)
somapar(numer)

