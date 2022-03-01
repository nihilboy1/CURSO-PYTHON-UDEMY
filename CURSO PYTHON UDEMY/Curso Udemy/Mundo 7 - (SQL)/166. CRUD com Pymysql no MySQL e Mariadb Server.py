import pymysql.cursors
from contextlib import contextmanager


# CRUD = Create, Read, Update and Delete

@contextmanager
def conecta():
    conexao = pymysql.connect(host='127.0.0.1',
                              user='root',
                              password='',
                              db='clientes',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        yield conexao
    finally:
        print('\n'
              'Conexão fechada')
        conexao.close()


'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
                  '(%s, %s, %s, %s)'
        cursor.execute(comando, ('Samuel', 'Severiano', 23, 85))
        conexao.commit()
        
# adicionar alguns valores
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
                  '(%s, %s, %s, %s)'

        dados = [('MURIEL', 'FIGUEIREDO', 19, 55,),
                 ('LUCAS', 'SILVA', 22, 60,),
                 ('KATIA', 'SILVA', 44, 91,),
                 ('KLAUDIAS', 'SEKMETH', 31, 61,),]

        cursor.executemany(comando, dados)
        conexao.commit()

# adicionar varios valores
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(comando, (6,))
        conexao.commit()

# deletar um item
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'DELETE FROM clientes WHERE id IN (%s, %s, %s, %s, %s)'
        cursor.execute(comando, (7, 8, 9, 10, 11))
        conexao.commit()
        
# apagar valores específicos
'''

"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(comando, (5, 15))
        conexao.commit()
        
# deletar dentro de um range
"""

"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        comando = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(comando, ('JHONNY', 3))
        conexao.commit()

# alterar um dado específico baseado no id
"""

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')  # aqui eu posso escolher qual coluna mostrar, em vez do *
        # também é possivel abreviar a chamada. por exemplo: nome como n
        # LIMIT 100 limita a quantidade de retornos que eu possivelmente teria nessa consulta (o limite vem por último)

        # ORDER BY ‘id’, name, ordena a minha consulta com base em algo.
        # Finalizo com DESC se quiser decrescente e com ASC para crescente

        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)  # no dicionário do banco de dados, a chave representa a coluna
