import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()
'''cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('maria', 80))  # assim é mais seguro
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("maria", 81)')  # assim tem o erro do sql injection
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Joana', 'peso': '150'})
conexao.commit()'''
'''cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'marieta', 'id': '2'})'''  # troca algo na base de dados
'''cursor.execute('DELETE FROM clientes WHERE id=:id',
               {'id': 5})''' # deleta um valor baseado no id
"SELECT nome, peso FROM clientes WHERE peso > 80"
cursor.execute('SELECT')
conexao.commit()
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    iden, nome, peso = linha
    print(iden, nome, peso)

cursor.close()
conexao.close()
