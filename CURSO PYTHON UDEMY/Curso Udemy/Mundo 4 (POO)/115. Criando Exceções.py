class ErradinError(Exception):
    pass


def teste():
    raise ErradinError('Errou rude!')


try:
    teste()
except ErradinError as erro:
    print(f'Erro: {erro}')
