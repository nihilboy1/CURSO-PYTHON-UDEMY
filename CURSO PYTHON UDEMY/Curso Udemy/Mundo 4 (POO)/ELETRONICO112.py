class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print('Já esta ligado')
            return
        else:
            print('Acaba de ser ligado')
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            print('Não posso deligar algo que não está ligado')
            return
        else:
            self._ligado = False
            print('Foi desligado!')