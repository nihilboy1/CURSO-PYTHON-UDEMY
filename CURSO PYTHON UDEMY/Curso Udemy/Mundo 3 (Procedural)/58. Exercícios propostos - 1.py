def func2():
    return 'olá'


def func1(a):
    return a()
# func1 é uma função que retorna a execução do seu parametro


ex = func1(func2)
print(ex)
print(type(func2))
