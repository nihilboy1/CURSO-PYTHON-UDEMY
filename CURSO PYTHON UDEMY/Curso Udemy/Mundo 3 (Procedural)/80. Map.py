from DATA import produtos, pessoas, lista
'''
n_lista = map(lambda x: x*2, lista)
#print(list(n_lista))

a função map() percorre uma lista executando uma função em cada item dela


'''


def aumentapreco(p):
    p['preco'] = round(p['preco'] * 1.07, 2)
    return p


nov_prod = map(aumentapreco, produtos)
for p in nov_prod:
    print(p)

'''
O ponto mais estranho aqui é o fato de que quanto eu jogo a lista ''produtos'' como parametro da função,
ela ja entra direto no meu primeiro dicionário. isso que eu n entendo. mas blz...
acredito que pra entrar no primeiro dicionário, deveria ser mostrado pra ela um produtos[0] em algum momento
'''
"""
def pessoa(a):
    return a['nome']


x = map(pessoa, pessoas)
for c in x:
    print(c)
"""
'''
mas pelo o que eu to vendo, ele só retorna ''desempacotando'' essa primeira lista, se for passando pelo map()
printando normal ele quebra, alegando que OBVIAMENTE tem uma lista ali no caminho
'''




