class Base_de_dados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for c, x in self._dados['clientes'].items():
            print(c, x)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

'''
Pela convensão do python, é altamente recomendado que, variaveis ou métodos que se iniciem com _ ou  __ não sejam alteradas

'''
bd = Base_de_dados()
bd.inserir_cliente(0, 'Ramiro')
bd.inserir_cliente(1, 'André')
bd.inserir_cliente(2, 'Otávio')
bd.inserir_cliente(3, 'Félix')
bd.apaga_cliente(1)
bd.listar_clientes()
