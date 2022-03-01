# preco = 50
#
# imposto = lambda x: preco * 30 / 100
# print(f'Aqui ele mostra que a variavel se tornou uma função: {type(imposto)}')
# print(f'Aqui eu executo a função e obtenho um resultado: {imposto(preco)}')
#

"""
o / lambda / é uma expressão indefinida que trabalha em cima de um parametro, 
retornando o produto de uma expressão e atribuindo ele a uma variavel que ganha a caracteristica de função 
me permitindo executar aquela variavel para obter o resultado final
"""

lista = [
    ['p1', 13],
    ['p2', 3],
    ['p4', 135],
    ['p3', 1],
    ['p5', 113]
]

lista.sort(key=lambda x: x[0])
print(F'{lista} // sort()')

"""
Esse / sort() / recebe uma função como parâmetro e 
usa ela como chave pra organizar uma lista

O QUE IMPORTA NO LAMBDA É O RETORNO!
"""
