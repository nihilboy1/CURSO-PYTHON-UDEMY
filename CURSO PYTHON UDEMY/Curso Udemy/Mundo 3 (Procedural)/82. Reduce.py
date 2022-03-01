from DATA import produtos, pessoas, lista
from functools import reduce
print('programa: ------------------------------------------------------------------\n')
soma_lista = reduce(lambda x, a:x + a, lista)
print(soma_lista)
# a função indefinida lambda tem os parametros "x" e "a", que retornam "x" + "a", onde "x" é igual a 0, 
# e "a" recebe os valores da lista em ordem
