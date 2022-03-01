nome = 'Samuel'
idade = 23
alt = 1.73
peso = 84.0
ano_atual = 2021
nasc = ano_atual - idade
imc = peso / alt ** 2
print('Olá! Seu nome é {}, sua altura é {}, sua idade é {}, Você pesa {}KG e nasceu no ano de {}. '
      '\nCom base nisso, posso afirmar que seu imc é {:.2f}.'.format(nome, alt, idade, peso, nasc, imc))
