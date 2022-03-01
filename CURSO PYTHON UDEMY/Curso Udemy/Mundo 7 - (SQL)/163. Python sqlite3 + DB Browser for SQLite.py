import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        comando = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(comando, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        comando = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(comando, (nome, telefone, id))
        self.conn.commit()

    def limpar(self, id):
        comando = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(comando, (id,))
        self.conn.commit()

    def listar(self):
        comando = 'SELECT * FROM agenda'
        self.cursor.execute(comando)
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        comando = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(comando, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('dadosparateste.db')
    '''agenda.inserir('Samuel', '8498725995')
    agenda.inserir('Samusel', '84493995')
    agenda.inserir('Samfuel', '849875595')
    agenda.inserir('Samuael', '8466995')
    agenda.inserir('Samguel', '849876995')'''
    agenda.buscar('sam')
