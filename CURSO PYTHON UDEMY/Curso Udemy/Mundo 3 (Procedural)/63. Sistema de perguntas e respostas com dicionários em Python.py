respcerta = 0
pergs = 0
perguntas = {
     'pergunta 1':
     {'pergunta': 'Quanto é 2+2?', 'respostas': {'a': '1', 'b': '4', 'c': '5', },
      'resposta_certa': 'b'},
     'pergunta 2':
     {'pergunta': 'Peixes voam?', 'respostas': {'a': 'Sim', 'b': 'Não', 'c': 'Talvez', },
      'resposta_certa': 'a'},
     'pergunta 3':
     {'pergunta': 'Qual o estado físico do gelo?', 'respostas': {'a': 'Sólido', 'b': 'Líquido', 'c': 'Gasoso', },
      'resposta_certa': 'a'},
     'pergunta 4':
     {'pergunta': 'Quem descobriu o Brasil?', 'respostas': {'a': 'P.A. Cabral', 'b': 'Seu Madruga', 'c': 'Eliel da padaria', },
      'resposta_certa': 'a'},
     'pergunta 5':
     {'pergunta': 'Qual a cor do cavalo vermelho de Napoleão?', 'respostas': {'a': 'Azul', 'b': 'Verde', 'c': 'Vermelho', },
      'resposta_certa': 'c'},
}
print('-' * 40)
for pk, pv, in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Alternativas:')

    for rk, rv in pv['respostas'].items():
        print(f' [{rk}] : {rv}')
    print()
    resp = input('Informe a resposta: ')
    pergs += 1
    if resp == pv['resposta_certa']:
        print('Resposta correta!')
        respcerta += 1
        print('Quantidade de perguntas até o momento: {} ||| Acertos: {}'.format(pergs, respcerta))
    else:
        print('Resposta errada!')
    print('-' * 40)
porc = respcerta / len(perguntas) * 100
print('Jogo finalizado: Você teve {:.0f}% de acertividade'.format(porc))
