class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando')


'''
Os métodos são chamados de dentro pra fora, das classes filhas para as mães.
Isso me permite reescrever um método de mesmo nome em uma classe diferente, 
mudando a sua finalidade
'''


class ClienteVIP(Cliente):
    def falar(self):
        super().comprar()
        Pessoa.falar(self)
        print('outra coisa')


"""
eu também posso chamar diretamente de uma classe especifica, 
preciso informar os paramentros // Pessoa.falar(self)
"""

'''
Se eu chamar a função "super()" dentro do método, ele vai atrás da execução
do método atrelado a ela, independente de em qual classe esteja 
(contanto que seja de uma clase de dentro da herança)
'''


class ClienteVIP2(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome}, {self.sobrenome}')

"""
Eu posso definir um novo construtor dentro de uma método de uma classe de herança
pra isso, vou precisar chamar, logo após, o construtor que ja está sendo a base,
para assim que eu receber os valores do meu construtor novo, eu poder os passar para ele.
depois eu defino os parametros diferentes que eu tenha criado
"""
