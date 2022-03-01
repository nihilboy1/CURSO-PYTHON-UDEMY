from itertools import groupby

alunos = [
    {'nome': 'luiz', 'nota': 'a'},
    {'nome': 'maria', 'nota': 'b'},
    {'nome': 'jose', 'nota': 'c'},
    {'nome': 'leticia', 'nota': 'a'},
    {'nome': 'fabricio', 'nota': 'd'},
    {'nome': 'mary', 'nota': 'f'},
    {'nome': 'joão', 'nota': 'a'},
    {'nome': 'fernando', 'nota': 'b'},
    {'nome': 'anderson', 'nota': 'c'},
    {'nome': 'lary', 'nota': 'a'},
]

ordena = lambda x: x['nota']
alunos.sort(key=ordena)
grupo_alunos = groupby(alunos, ordena)
'''
Nesse código acima, pelo o que eu entendi, a função lambda retorna um parametro indefinido
atrelado a um indice para a variavel ''ordena''
após isso, eu chamo essa variavel como parâmetro no meu sort(), que vai aplicar isso no ''alunos'', 
que é a variavel na qual ele foi chamado, retornando a lista, ordenada pela 'nota'
abaixo, temos a variavel ''grupo_alunos'' recebendo o groupby() com os parametros ''alunos'' e ''ordena''
o groupby() vai armazenar, baseado no valor do indice passado pra ele através do parametro que carrega a função ''ordena''
todos os elementos que estão dentro de ''alunos''
'''
for agrup, v_agrup in grupo_alunos:
    print(agrup)
    for aluno in v_agrup:
        print(f'{aluno}')
    print()

