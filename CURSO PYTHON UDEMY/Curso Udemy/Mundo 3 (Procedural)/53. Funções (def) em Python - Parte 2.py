"""
def funcao(var):
    print(var)


v = funcao('Olá')
print(v)

# se eu adicionar à uma variavel o produto de uma função que não possua / return /, a variavel vai receber / none /, que representa 'nada'
"""


def funcao(var):
    return (var)


v = funcao('Olá')
print(v)

# o / return / adiciona o produto da minha função à ela mesma ou a uma variavel que à receba
#após o / return / nada mais é executado dentro da função. isso da margem para adicionar mais de um return dentro da função



def f(var):
    print('Olá')

def g():
    return f

v = g()

print(v(1))
#é possivel até atribuir uma função a uma variavel, usando duas funções (bagulho estranhão)