nome = str(input('Escreve seu primeiro nome: '))
cont = len(nome)
if cont <= 4:
    print('Você escreveu: - {} - Seu nome tem {} letras e ele é considerado Curto!'.format(nome, cont))
if 5 < cont <= 6:
    print('Você escreveu: - {} - Contendo {} letras, seu nome é considerado Médio!'.format(nome, cont))
if cont > 6:
    print('Com {} letras, você tem um nome grande! Nome informado: - {} -'.format(cont, nome))