def divive(a, b):
    try:
        return a / b
    except ZeroDivisionError as Error:
        print('Log: ', Error)
        raise


# eu posso usar o except pra guardar esse meu erro dentro de um log
# e ainda assim, retornar o erro pro usuário usando o raise


def divive2(a, b):
    if b == 0:
        raise ValueError('"b" não pode ser 0')
    return a / b
# usando ValueError eu consigo mexer no retorno em texto da exceção


print(divive2(2, 1))
