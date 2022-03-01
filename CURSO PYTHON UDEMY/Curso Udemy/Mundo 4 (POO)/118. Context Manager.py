class Arqv:
    def __new__(cls, arquivo, modo):
        print('Entrou no __new__')
        """
        aqui eu crio a classe recebendo "arquivo" e "modo"
        """
        return object.__new__(cls)

    def __init__(self, arquivo, modo):
        print('Entrou no __init__')

        """
        aqui eu inicio a classe com o parâmetros "arquivo" e "modo"
        que vieram do __new__
        """
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou no __enter__')
        """
        Esse método serve para quando eu chamar o "with" com o nome da minha classe
        dai ele vai procurar se esse método existe dentro dela, pra saber o que ele deve usar
        pra criar o arquivo
        """
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Entrou no __exit__')
        """
        só sei que fecha automaticamente, pq o professor n explicou
        """
        self.arquivo.close()
        '''
        exc_type, exc_val, exc_tb
        esses parâmetros acima são pra tratar exceções
        e após tratalas, eu devo terminar o código com um
        return True
        '''


with Arqv('abb.txt', 'w+') as file:
    file.write('olá, olá')
