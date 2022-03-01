s1 = {1, 2, 3}
s1.add(1)
s1.discard(3)
print(s1)
# conjuntos, assim como tuplas, são imutaveis
s1.update('python')
print(s1)
# após usar um .update no set, ele embaralha todos os itens
s1.update([1, 2, 3, 4, 5], {'za', 'ae', 5})
print(s1)
# sets não aceitam elementos duplicados e ele também desfaz quelquer lista, dicionário ou tupla que seja inserida nele
# transformando tudo em itens unicos
# bom lembrar dessa ferramenta pra tirar itens duplicados de uma lista
s2 = {1, 9, 5, 2, 6}
s3 = s1.union(s2)
print(s3)
# essa função / union() / une os dois sets, discartando valores repetidos.
# ela também pode ser repesentada com aquela barra reta: |
s3 = s1 & s2
print(s3)
# o & retorna os valores identicos presentes em ambos os sets
s3 = s2 - s1
print(s3)
# usar o sinal de - comparando sets retorna os valores que são unicos apenas ao conjuto da esquerda
s3 = s2 ^ s1
print(s3)
# o sinal de ^ me mostra quais os itens são unicos para ambos um dos sets






