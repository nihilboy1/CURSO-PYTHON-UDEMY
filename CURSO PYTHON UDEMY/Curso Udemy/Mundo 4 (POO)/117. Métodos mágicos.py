# dunder == doubleunderscore

"""
LISTA DE MÉTODOS MÁGICOS
https://rszalski.github.io/magicmethods/
"""
'''
x = A(1, 2, 3, x=4)

x = A.__new__(A, *args, **kwargs) # Aqui "x" é instanciado em "A", recebendo seus argumento
if isinstance(x, A): # aqui ele testa se ela foi instanciado corretamente
    type(x).__init__(x,*args, **kwargs) # aqui ele inicializa a nova instância com seus argumentos

__new__ é quem cria o novo objeto de fato (sendo obrigado a sempre retornar algo)
__init__ apenas inicia ele
'''


class A:
    def __init__(self):
        print('Iniciou a classe A')
        '''
        Só de eu instânciar essa classe em a,
        ela ja executa tudo que estiver dentro de __init__
        '''


# a = A()


class B:
    def __new__(cls, nome, idade):
        cls.nomex = 'oi'  # atributo DE CLASSE
        print('criou o objeto com o __new__')

        def haha(*args, **kwargs):
            """
            quando eu defino um método de classe aqui no new, ele ja envia o self como parâmetro,
            então eu tenho que usar os *args, **kwargs pra segurar esse self que foi enviado
            """
            print('rodou o haha que eu criei no __new__ e chamei na instância')

        cls.haha = haha

        return object.__new__(cls)  # isso aqui é o que importa, retorno após a criação do objeto

    def __init__(self, nome, idade):
        print('a classe inicou de fato agora com o __init__')


b = B('luiz', 18)
b.haha()

"""
__call__ transforma minha classe numa função
"""
"""
__setattr__ sempre que eu tentar setar um atributo à minha classe 
atráves da minha instância, esse método vai interceptalo e poder tratalo
"""
"""
__del__ é chamado quando o python deleta algo
"""
"""
___str__ é chamado quando eu tento chamar a minha instância como string
dai eu posso colocar uma mensagenzinha
"""

"""
o método ___len__ é executado quando eu tento chamar o len() na minha classe
dai eu posso configurar a saída de dentro dele
"""
