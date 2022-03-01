print('\n')



try:
# eu posso identar quanto try eu quiser
    print(a)
except Exception as erro:
    print(f'Ocorreu um erro: {erro}')
# assim eu sinalizo pra qualquer tipo de erro.
else:
    print('Nenhum erro encontrado')
# o else, depois do try, só é executado se o código em questão, rodar sem erro.
finally:
    print('Sempre será executado!')
# o finally sempre é executado, independente de ter dado erro ou não
