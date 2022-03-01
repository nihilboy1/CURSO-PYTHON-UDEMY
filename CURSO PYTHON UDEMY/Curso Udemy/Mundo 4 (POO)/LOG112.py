class Logmixing:
    @staticmethod
    def escreve(msg):
        with open('log.txt', 'a+') as file:
            file.write(msg)
            file.write('\n')

    '''
    Como dentro do método eu não precisei usar o self. em nenhum atributo
    eu posso passar ele como método estático
    '''
    def log_info(self, msg):
        self.escreve(f'INFO: {msg}')

    def log_error(self, msg):
        self.escreve(f'ERROR: {msg}')