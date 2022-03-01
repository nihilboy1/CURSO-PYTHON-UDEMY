import arquivos


def organiza_e_mostra(a):
    print('\nTarefas adicionadas até o momento: ')
    for c in a:
        print(f'{c}')
    print()


def undo(a, b):
    a.append(b[-1])
    if b:
        b.pop()
    else:
        print('Não existem mais valores na lista!')


def redo(a, b):
    if a:
        b.append(a[-1])
        a.pop()
    else:
        print('Não há itens para serem recuperados!')


def addtarefa():
    x = str(input('Adicione uma nova tarefa: '))
    arquivos.listatop.append(x)
    arquivos.nuncaapaga.append(x)


print('ORGANIZADOR DE TAREFAS!')
while True:
    escolha = int(input('--------------------------------------------\n'
                        'Listar tarefas: [0]\n'
                        'Adicionar tarefas: [1]\n'
                        'Excluir ultima tarefa adicionada: (undo) [2]\n'
                        'Desfazer ultima exclusão: (redo) [3]\n'
                        'Informe: '))
    if escolha == 0:
        organiza_e_mostra(arquivos.listatop)
    elif escolha == 1:
        addtarefa()
        organiza_e_mostra(arquivos.listatop)
    elif escolha == 2:
        undo(arquivos.itensapagados, arquivos.listatop)
        organiza_e_mostra(arquivos.listatop)
    elif escolha == 3:
        redo(arquivos.itensapagados, arquivos.listatop)
        organiza_e_mostra(arquivos.listatop)
