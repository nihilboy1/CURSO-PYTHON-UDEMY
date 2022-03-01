import sys
import time

lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)
# print(hasattr(lista, '__next__'))
"""
se eu atribuir esse metodo iter a minha lista, ela vira um iterador
e eu posso usar a função next para executar ela em partes
"""
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
"""
esse next aí serve pra executar meu iterador em partes

"""
lista = list(range(10))
# print(sys.getsizeof(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))
# for v in g:
    # print(v)

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
print(l2)
# nesse caso, o l2 é um ''gerador'', e ele não armazena tudo na memoria do pc
# ele só vai rodar esses numeros, se eu pedir com a função next, ou abrindo um for.
# o gerador também é um iterador

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

