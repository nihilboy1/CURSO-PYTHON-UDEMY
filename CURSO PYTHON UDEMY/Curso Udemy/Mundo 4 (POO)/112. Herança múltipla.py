class A:
    def falar(self):
        print('Oi estou em A')


class B(A):
    def falar(self):
        print('Oi estou em B')


class C(A):
    def falar(self):
        print('Oi estou em B')


class D(B, A):
    pass


d = D()
d.falar()
'''
Quando eu faço o tipo acima de herança mulpipla, (ou seja, herdo de A para B e C,
e depois herdo B e C para D.) quando eu chammo um método através de D, ele vai seguir a ordem que foi informada nos
parametros para achar o método. Nesse caso, ele entra logo em B
'''
