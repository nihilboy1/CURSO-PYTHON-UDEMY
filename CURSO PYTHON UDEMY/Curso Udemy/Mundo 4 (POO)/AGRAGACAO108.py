class Carrinho_de_compras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for x in self.produtos:
            total = total + x.valor
            return total


'''
Eu não consigo desempacotar uma lista dentro de duas variaveis num for aqui nas classes
eu tenho que chamar pra dentro de uma só, e depois, qd for tratar ela, eu especifico com qual método eu quero lidar
'''


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
