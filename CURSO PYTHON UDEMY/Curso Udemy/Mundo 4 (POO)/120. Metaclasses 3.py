print('\n')

'''
a classe type, é de onde se herda para criar classes
'''
class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr': 'Olá, mundo'})

a = A()
print(a.attr)
print(a.nome)