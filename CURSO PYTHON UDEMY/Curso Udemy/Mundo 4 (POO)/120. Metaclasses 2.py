print('-')
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobreescrever o atributo!')
            del namespace['attr_classe']
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass = Meta):
    attr_classe = 'Correto A'
    
class B(A):
    attr_classe = 'Errado B'
     
b= B()
print(b.attr_classe)
