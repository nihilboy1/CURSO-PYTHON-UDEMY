from contextlib import contextmanager

'''
Importando esse múdulo acima, eu não preciso criar a classe
pra fazer o gerenciador de contexto
'''


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo!')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('KK3K.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 3\n')
    file.write('Linha 3\n')
