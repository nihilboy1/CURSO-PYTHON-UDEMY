def cronos(a, b, c):
    from time import sleep
    print('Contagem de {} a {} com passo de {}'.format(a, b, c))
    for c in range(a, b+1, c):
        print(c, end=' ')
        sleep(0.3)
    print('\n')


ini = 0
fim = 10
passo = 1
cronos(ini, fim, passo)
ini = 10
fim = 0
passo = -2
cronos(ini, fim, passo)
ini = int(input('Informe o inicio da contagem: '))
fim = int(input('Informe o fim da contagem: '))
passo = int(input('Informe o ''passo'' da contagem: '))
cronos(ini, fim, passo)



