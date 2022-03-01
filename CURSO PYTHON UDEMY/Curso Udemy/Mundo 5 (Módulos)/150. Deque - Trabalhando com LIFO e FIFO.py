'''
Como funciona o sistema de armazenagem LIFO?
A sigla LIFO, em inglês, quer dizer “Last in, First Out”.
Ela refere-se a um sistema onde os produtos que entraram há mais tempo no estoque são os primeiro a serem vendidos.

Como funciona o sistema de armazenagem FIFO?
Elucidando o assunto, a sigla FIFO em inglês quer dizer “First in, First Out”.
Isso quer dizer que as primeiras das mercadorias a entrarem no armazém são as primeiras a serem vendidas.
'''

from collections import deque

fila = deque(maxlen=10)  # esse atributo limita a quantidade de valores no deque
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)
fila.append(6)
fila.append(7)
fila.append(8)
fila.append(9)
fila.append(10)
fila.append(11)
print(fila)
