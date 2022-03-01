from random import randint


class X:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nasc(self):
        print(self.ano_atual - self.idade)

    @classmethod  # isso aqui serve pra marcar que esse método só pode ser chamado pela classe
    def por_ano(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera():
        return randint(1, 999)


p1 = X.por_ano('João', 1998)
'''
os métodos de classe, devem ser chamados nas classes, 
para poder alterar os parametros padrão que estão sendo pedidos
'''
#
print(X.ano_atual)
'''
Apesar da variavel "ano_atual" estar disponivel para todas as funções da classe
ela é propriedade da classe em si
'''
print(p1.idade)
'''
um método de instância tem a ver com as informações da instância, enquanto um método da classe, não
'''
print(p1.gera())
print(X.gera())

'''
os métodos estáticos não pretendem chamar nem parametros da classe nem das intâncias
eles vão ser independentes, gerando valores auto-suficientes
'''
