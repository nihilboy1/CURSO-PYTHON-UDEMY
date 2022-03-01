def soma(x, y):
    return x + y


print(f'independente do __main__: ', soma(1, 2))
'''
essa linha de código acima vai rodar em todo canto que estiver importando o módulo
pra acabar com isso, eu posso testar o nome do módulo
'''
if __name__ == '__main__':
    print('dentro do __main__', soma(3, 5))
print(f'sendo executado a partir do: ', __name__)
'''
esse print aparece independente de onde esse módulo seja executado
'''
