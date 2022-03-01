from COMPOSICAO109 import Cliente, Endereco

'''
Composição é quando uma classe é dona da outra
'''
cliente1 = Cliente('João', 32)
cliente1.insereendereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listaendereco()
print()

cliente2 = Cliente('Maria', 50)
cliente2.insereendereco('Natal', 'RN')
cliente2.insereendereco('Rio de janeiro', 'RJ')
print(cliente2.nome)
cliente2.listaendereco()
print()

cliente3 = Cliente('Mary', 10)
cliente3.insereendereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.listaendereco()
print()
