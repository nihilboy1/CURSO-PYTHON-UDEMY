from DATA import pessoas, produtos, lista

n_lista = filter(lambda x: x['preco'] > 100, produtos)

for c in n_lista:
    print(c)