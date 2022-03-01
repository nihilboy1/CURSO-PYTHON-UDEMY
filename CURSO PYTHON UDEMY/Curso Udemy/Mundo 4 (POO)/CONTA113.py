from abc import ABC, abstractmethod


class Conta(ABC):
    '''
    Aqui eu vou atribuir à minha classe "Conta" a possibilidade de
    criar métodos abstratos, tornando ela, uma classe abstrata, que também
    não pode ser instânciada
    '''

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")
        else:
            self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")
        print(f'O valor depositado foi de: {valor}')
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}')
        print(f'Conta: {self._conta}')
        print(f'Saldo: {self._saldo}')

    '''
    Aqui eu crio um método abstrado, que tem que ser criado obrigatóriamente
    em qualquer classe filha 
    '''

    @abstractmethod
    def sacar(self, valor):
        pass
