# 12454722402
from math import floor
from time import sleep
from random import randint
while True:
    cpflist = []
    results1 = []
    """
    Aqui dentro o usuário informa o cpf
    e eu só passo pra próxima parte quando ele estiver limpo
    cpfusu = str(input('Informe um CPF para ser analisado: ')).strip().replace('.', '').replace('-', '')
    c = len(cpfusu)
    cpflimpo = cpfusu if cpfusu.isnumeric() and c == 11 else print('Entrada inválida!')
    if cpflimpo:
        cpf1 = cpflimpo[0:9]
    else:
        print('Informe apenas 11 digitos, e todos sendo numeros')
        continue
    """
    cpf1 = str(randint(100000000, 999999999))
    """
    Agora começa o loop, onde eu vou multiplicar os numeros, guardar eles nas listas
    e depois somalos
    """
    print('Analisando primeiro dígito do CPF...')
    sleep(0.5)
    multi = 10
    for num in cpf1:
        cpflist.append(num)
        numint = int(num)
        result = numint * multi
        results1.append(result)
        multi = multi - 1
    soma1 = sum(results1)
    divi = soma1 / 11
    resto = soma1 - (11 * floor(divi))
    if resto < 2:
        digito1 = 0
    elif resto > 1:
        digito1 = 11 - resto
    elif resto > 11:
        continue
    cpf2 = str(cpf1) + str(digito1)
    """
    Calculando o outro digito
    """
    print('Analisando segundo dígito do CPF...')
    sleep(0.5)
    cpflist = []
    results1 = []
    multi = 11
    for num in cpf2:
        cpflist.append(num)
        numint = int(num)
        result = numint * multi
        results1.append(result)
        multi = multi - 1
    soma1 = sum(results1)
    divi = soma1 / 11
    resto = soma1 - (11 * floor(divi))
    if resto < 2:
        digito1 = 0
    elif resto > 1:
        digito1 = 11 - resto
    elif resto > 11:
        continue
    cpf3 = str(cpf2) + str(digito1)
    print('Foi gerado um novo CPF aleatório: {}\n'.format(cpf3))
    sleep(1.5)



        

    
         
         
    
