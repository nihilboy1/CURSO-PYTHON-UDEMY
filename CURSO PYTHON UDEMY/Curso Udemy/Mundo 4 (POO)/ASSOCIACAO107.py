class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
        '''
        Aqui eu defino uma ferramenta para o escritor, mas não identifico ela
        '''

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor




class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    def escrever(self):
        print('Caneta está escrevendo!')

    @property
    def marca(self):
        return self.__marca


class Maquina_de_escrever:
    def __init__(self):
        pass

    def escrever(self):
        print('Máquina está escrevendo!')
