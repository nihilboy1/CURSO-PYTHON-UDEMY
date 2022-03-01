from abc import ABC, abstractmethod


class A(ABC):
    """
    Chamar um método abstrado dentro de uma classe, significa que aquela classe
    não deve ser instanciada diretamente, obrigando as classes "filhas" a sobreescreverem
    esse mesmo método, caso pretendam usalo
    A classe "A" torna-se apenas um local abstrado
    """

    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('B falando')


x = B()
x.falar()
