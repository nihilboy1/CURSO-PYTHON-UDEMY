from CONTA113 import Conta  # Conta é uma classe abstrata


class Conta_Corre(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        Conta.__init__(self, agencia, conta, saldo)
        self._limite = limite

        @property
        def limite(self):
            return self._limite

    '''
    Aqui eu crio o método abstrado que me foi obrigado pela classe ''Conta''
    '''

    def sacar(self, valor):
        if self._limite < valor:
            print('Valor de saque diário excedido!')
        elif valor > self._saldo:
            print('Valor de saque indisponivel!')
        else:
            self._saldo -= valor
            print(f'Valor sacado: {valor}R$')
            self.detalhes()
