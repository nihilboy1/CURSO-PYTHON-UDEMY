from AGRAGACAO108 import Carrinho_de_compras, Produto
'''
Agragação é quando uma classe é dependente da outra
'''
carrinho = Carrinho_de_compras()

x1 = Produto('Macarrão', 5)
x2 = Produto('Banana', 2)
x3 = Produto('Salada', 3)
x4 = Produto('Peperoni', 10)
x5 = Produto('Batata', 1)
carrinho.inserir_produto(x1)
print(carrinho.soma_total())

'''
agragações são classes co-dependentes
'''

