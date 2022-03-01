class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcen):
        self.preco = self.preco - (self.preco * porcen / 100)
        return str(f'{self.preco:.2f}').replace('.', ',')

    # Getter
    @property
    def preco(self):
        return self._preco

    '''
    Assim que qualquer valor for chamado através do "self.preco", antes
    o valor vai ser pego aqui para tratamento
    
    o getter faz a função se comportar como atributo
    se eu adicionar o Property no método e tentar chamar o método numa instancia
    ele vai entender que aquilo é apenas um atributo, e não um método
    '''

    # Setter
    @preco.setter
    def preco(self, valor):
        print(valor)
        if isinstance(valor, str):
            valor = float(valor.replace('-', ''))
        self._preco = valor

    '''
    aqui o valor vai ser tratado
    o primeiro parametro ( valor ) do setter, recebe o return do getter
    '''


# a = Produto('bolsa', 30000)
b = Produto('Calça', '--30')
# print(b.desconto(30))
# print(a.desconto(50))
