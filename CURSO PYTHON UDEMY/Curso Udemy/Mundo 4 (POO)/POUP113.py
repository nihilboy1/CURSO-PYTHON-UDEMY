from CONTA113 import Conta


class Conta_Poup(Conta):
    '''
    Aqui eu crio o método abstrado que me foi obrigado pela classe ''Conta''
    '''

    def sacar(self, valor):
        if self._saldo < valor:
            print('Valor de saque indisponivel!')
        else:
            self._saldo -= valor
            print(f'Valor sacado: {valor}R$')
            self.detalhes()