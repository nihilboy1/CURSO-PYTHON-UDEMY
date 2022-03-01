from ELETRONICO112 import Eletronico
from LOG112 import Logmixing


class Smartphone(Eletronico, Logmixing):
    def __init__(self, nome):
        Eletronico.__init__(self, nome)
        self.conectado = False

    '''
    Quando eu chamo uma classe dentro de outra, eu preciso, no inicializador
    da minha classe 2, chamar os mesmos parâmetros que estão presentes da minha classe1
    
    class Smartphone(Eletronico):
    def __init__(self, nome):
        Eletronico.__init__(self, nome)
    
    Depois eu também tenho que chamar o inicializador da classe1 pra repassar esses parâmetros
    dai eu continuo o código, podendo colocar novos estados pra minha classe2
    '''

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} Não está ligado!'
            print(info)
            self.log_error(info)
        if self.conectado:
            info = f'{self._nome} já está conectado'
            print(info)
            self.log_error(info)
        else:
            self.conectado = True
            info = f'{self._nome} foi conectado'
            self.log_info(info)

    def desconectar(self):
        if not self.conectado:
            info = f'{self._nome} Já está desconectado'
            print(info)
            self.log_error(info)
        else:
            self.conectado = False
            info = f'{self._nome} foi desconectado'
            print(info)
            self.log_info(info)
