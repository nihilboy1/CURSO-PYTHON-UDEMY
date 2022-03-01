"""
É possivel chamar um método da classe filha, através da classe pai
class A:
    def fala(self):
        self.b_fala()

class B:
    def b_fala(self)
        print('oi')

b = B()
b.fala()
resultado:
'oi'
"""
print()


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Não tem o método "b_fala" em {name}!')
        else:
            if not callable(namespace['b_fala']):
                print(f'"b_fala" deve ser um método! erro em {name}')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):  # todas as classes derivadas de A, estão sendo criadas baseadas na metaclasse
    def __new__(cls, nome, idade):
        return object.__new__(cls)

    def __init__(self, nome, idade):
        print('entrou')
        pass

    def fala(self):
        self.b_fala()


class B(A):
    pass
    # def b_fala(self):
    # print('oi')


class C(A):
    b_fala = 'w'
    pass
    # def b_fala(self):
    # print('oi')


a = A('nome', 18)
