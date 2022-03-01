"""
#while é um loop que segue realizando a mesma ação enquanto a condição testada for verdade
# CONTINUE faz o loop voltar pro inicio, sem executar o que vem em baixo.
                  # nesse caso, fazendo o programa printar e infinitamente
x = 0
while x < 5:
    if x == 3:
        print('3!')
        continue
    print(x)
    x = x + 1
print('Fim!')
"""




"""
#Ja nesse caso, usando BREAK, quando o computador ler essa expressão, ele logo encerra o laço
x = 0
while x < 5:
    if x == 3:
        print('3!')
        break
    print(x)
    x = x + 1

print('Fim!')
"""

"""
#while dentro de while
y = 0
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(x,'-', y)
        y = y + 1
    x = x + 1
print('fim')
"""
"""
#TABUADA  BÁSICA
calc = 0
num = int(input('Informe um numero: '))
while calc < 11:
    print('{} * {} É IGUAL A {}'.format(num, calc, num * calc))
    calc = calc + 1 
"""
