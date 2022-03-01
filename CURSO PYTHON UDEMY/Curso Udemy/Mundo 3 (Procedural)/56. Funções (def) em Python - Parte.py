"""
def func(a1, a2='casa', a3,):
    print(a1, a2, a3)

#Se eu nomear um parametro, os seguintes também devem ser nomeados.
"""

lis = [1, 2, 3, 4, 5]
print(*lis, sep=' ')

#Se eu usar o / * / eu posso desempacotar uma lista,mt top


tuple()
list()
dict()
#eu posso alterar o tipo de listas, tuplas e dicionarios usando as funções acima


def funca(*args, **kwargs):
    print(args)
    id = kwargs.get('idade')
    if id is not None:
        print(id)


funca('kk',kk='Olá', idade='20')


# / *args / recebe todos os argumentos não nomeados, enquanto / **kwargs / recebe todos os nomeados
# com a função / get() / eu consigo achar um valor especifico dentro dos parametros de tamanho indefinido