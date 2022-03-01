"""
def master():
    def slave():
        print('oi')
    slave()


print('Executando a master abaixo')
master()
'''
se eu simplesmente chamar a master(), nada acontece, pq ela só ta criando a slave()
pra que algo ocorra, eu preciso chamar a execução da slave
'''


def master2():
    def slave():
        print('oi')
    return slave


print('Executando o retorno da master abaixo')
retorno = master2()
retorno()
'''
Já aqui nesse caso, eu to atribuindo à minha variável, 
a possibilidade de ser uma função, sem executala 
'''

def master2(p):
    def slave():
        p()
    return slave


def fala_oi():
    print('oi')


print('Executando o retorno da master, que está recebendo como parâmetro a fala_oi()')
retorno = master2(fala_oi)
retorno()
"""


def master3(p):
    def slave():
        print('Passou dentro da função')
        p()

    return slave


@master3
def fala_oi():
    print('oi')


fala_oi()
print('Dentro do master sem atribuir à nenhuma variavel')
