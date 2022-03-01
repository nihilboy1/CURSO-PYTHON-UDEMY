"""
Polimorfismo é o principio que permite que classes derivads de uma mesma
superclass, tenham métodos iguals (de mesma assinatura)
mas comportamentos diferentes

mesma assinatura = Mesma quantidade e tipos de parâmetros
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B está falando: {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando: {msg}')


b = B()
c = C()

b.fala('oi')
c.fala('tchau')