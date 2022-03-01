class Cliente:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
        self.enderecos = []

    def insereendereco(self,cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    '''
    Se vc chamar uma classe dentro da outra e apagar a classe "mãe"
    a classe nova também é apagada junto, numa relação de composição
    '''
    def listaendereco(self):
        for enderecos in self.enderecos:
            print(enderecos.cidade, enderecos.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.estado} foi apagado')
