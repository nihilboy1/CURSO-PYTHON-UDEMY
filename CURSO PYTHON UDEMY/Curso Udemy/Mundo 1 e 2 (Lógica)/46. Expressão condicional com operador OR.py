nome = input('Qual seu nome? ')
print(nome or 'Você não digitou nada!')
# o python só vai executar o código acima se ele encontrar uma expressão verdadeira


a = 0
b = None
c = False
d = []
e = {}
f = 1
g = 'samu'
var = a or b or c or d or e or f or g
print(var)
# Aqui, assim como no primeiro exemplo, o python só vai atribuir a variavel
# se ela retornar um valor / True /