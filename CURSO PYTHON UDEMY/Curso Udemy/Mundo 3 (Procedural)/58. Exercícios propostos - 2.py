def func1(a, *b, **c):
    return a(*b, **c)


def func2(a2):
    return f'FUNC2 {a2}'


def func3(a3, b3):
    return F' FUNC3 {a3} E {b3}'


ex = func1(func3,'KKKKK', b3='BRIO')
print(ex)

"""
esse código funciona baasicamente igual ao anterior, com uma função recebendo como seu paramentro, outra função
entretanto, usando os / *args /  e / **kwargs // eu também consigo informar parametros para a função que será executada  
"""
