class Pessoa:
    def falar(self):
        print('oi')


'''
O self é um paramentro que é exclusivo para métodos de classes 
e ele referencia a instância que vai chamar a classe
por exemplo

x = Pessoa()
aqui, e to atribuindo a x, a classe Pessoa()

x.falar()
Aqui eu to chamando o método "falar()", da classe "Pessoa()" que foi atribuido a instância "x". 
No caso, o método sabe que é pra executar em x e não em outra instância que tenha recebido a classe, por causa do "self"
que está descrito no método da classe e que nesse caso, recebeu x.
'''


class Pessoas1():
    anoatual = 2020
    '''
    aqui eu estou atribuindo uma variavel que pode ser chamada por qualquer instancia da classe
    independente do método
    '''
    def __init__(self, nome, idade, comendo=False, falando=False):
        '''
        O init é uma método mágico, que é executado automaticamente quando a classe é instânciada
        nele eu posso solicitar parametros e atribuir valores padrão
        '''
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.a = 'a'
        print(self.a)

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
        elif self.falando:
            print(f'{self.nome} parou de falar!')
            self.falando = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo...')
        elif self.falando:
            print(f'{self.nome} já está falando...!')
        else:
            print(f'{self.nome} está falando {assunto}')
            self.falando = True

    '''
    Usar o "self" é o mesmo que informar a instancia que está chamando a classe
    '''

    def outro_metodo(self):
        print(self.a)

    '''
    Se eu criar uma variavel dentro de um método, ela tem escopo local,
    e eu só posso chamalá dentro de outro método da mesma classe se me referenciar a mesma
    com o "self" como mostrado acima
    '''

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já comeu!')
        elif self.falando:
            print(f'{self.nome} não consegue comer falando')
        else:
            print(f'{self.nome} está comendo um(a) {alimento}')
            self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
        elif self.comendo:
            print(f'{self.nome} parou de comer!')
            self.comendo = False

    '''
    Aqui eu uso um "if" pra mudar o estado de um dos parâmetros 
    '''
    def get_ano_de_nasc(self):
        return self.anoatual - self.idade
