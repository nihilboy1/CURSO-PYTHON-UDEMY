v = 'valor'


def func():
    print(v)


func()
# uma variavel atribuida fora do / def / é global, e pode ser chamada dentro dele
x = 'ooo'


def funx():
    global x
    x = 'aaa'
    print(x)


funx()
# alterar o valor de uma variavel já existente dentro de uma função, cria uma nova variavel, dessa vez, de escopo local
# o unico jeito de alterar o valor de uma variavel de dentro de uma função é usando o / global /
# não é possivel referenciar uma variavel global dentro do / def / caso eu queira alterar seu valor no escopo local
