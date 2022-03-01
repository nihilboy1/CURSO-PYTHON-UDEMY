'''
d1 = {0: 1, 'a': float(), (1, 2): True}
# chegando nos valores usando as chaves estranhas
print(d1[(1, 2)])
# alterando valores no dicionario original
d1.update({'Novachave': 'add' })
print(d1)
d1['newkey'] = 'ADD'
print(d1)
# checando se objetos existem no dicionario
print(0 in d1.keys())
print(float() in d1.values())
# a função / len() / conta a quantidade de pares no dicionario
print(len(d1))
"""
Dicionários são como listas, mas aqui, eu posso determinar quais serão os valores do meu indice
"""
# correndo um / for / sobre o dicionário
d2 = {
    'chave1': 1,
    'chave2': 2,
    'chave3': 3,
    'chave4': 4,
}
for k in d2.keys():
    print(k)
# eu posso usar as funções / keys(), values() e items() / para especificar por quais objetos eu quero iterar o / for /
'''
clientes = {
    'cliente1': {'nome': 'Luiz', 'idade': 17},
    'cliente2': {'nome': 'João', 'idade': 15},
    'cliente3': {'nome': 'Maria', 'idade': 20},
    'cliente4': {'nome': 'Elen', 'idade': 22},}
"""
for a, b in clientes.items():
    print(a)
    for d, x in b.items():
        print(f'\t {d}, {x}'.replace(',', ':'))
"""
v = clientes
x = clientes.copy()
# Se eu atribuir o dicionário a uma variavel e tentar mudar algo no dicionário através da variavel
# o dicionário original também será alterado. o que pode-se fazer para copiar um dicionário é
# usar a função / copy() / mas ela é uma ''cópia rasa''
# o correto é importar o módulo copy e usar a função deepcopy()

# é possivel converter uma lista ou uma tupla para um dicionário, contanto que eles possuam
# duplas que possam servir de chave e valor


















