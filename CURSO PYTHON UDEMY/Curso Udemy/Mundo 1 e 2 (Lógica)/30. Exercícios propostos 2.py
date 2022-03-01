hora = input('Informe o horário! ')
teste_hora = hora.isdigit()
if teste_hora:
    horaint = int(hora)
    if 0 == horaint <= 11:
        print('Agora são {} da manhã! Tenha um bom dia!'.format(horaint))
    elif 11 < horaint <= 17:
        print('Agora são {} da tarde! Tenha uma boa tarde!'.format(horaint))
    elif 17 < horaint <= 23:
        print('Agora são {} da noite! Tenha uma boa noite!'.format(horaint))
    else:
        print('Entrada inválida! Informe um numero entre 0 e 23')

elif not teste_hora:
    print('Entrada inválida! Informe um numero entre 0 e 23!')


