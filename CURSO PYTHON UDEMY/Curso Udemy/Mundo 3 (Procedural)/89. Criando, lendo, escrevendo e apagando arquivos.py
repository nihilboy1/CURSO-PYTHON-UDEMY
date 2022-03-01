file = open('abc.txt', 'w+')  # esse w+ cria limpa o arquivo e cria ele de novo
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.seek(0, 0)  # esse file seek em 0,0 indica que eu quero ler tudo
print(file.read())  # aqui ele lê to-do o arquivo
file.seek(0, 0)
print(file.readline())  # esse aqui lê linha por linha
print(file.readline()) # e como esse valor é um iteravel, eu posso abrir um for nele
file.close()
