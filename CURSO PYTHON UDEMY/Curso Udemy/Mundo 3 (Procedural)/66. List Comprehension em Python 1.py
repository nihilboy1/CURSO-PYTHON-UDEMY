'''
def multi(a, b):
    return a * b


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [var * 2 for var in l1]
print(ex1)
# ex1 recebe, pra cada var em l1, var * 2
ex2 = [multi(var, 2) for var in l1]
# ex2 recebe, pra cada var em l1, o retorno da função multi sobre var e 2
print(ex2)
ex3 = [valor for valor in l1 if valor > 5]
print(ex3)
# ex3 recebe, pra cada valor em l1, o valor, se valor > 5
ex4 = [valor if valor != 5 else 'opa' for valor in l1 if valor % 2 != 0]
print(ex4)
# ex4 recebe, pra cada valor em l1, o valor, se valor % 2 != 0.Se se valor != 5, valor recebe 'opa'

FOR DENTRO DE FOR

l_c = [(x, y) if y == 3 else 'YPSISON'for x in range(1, 11) for y in range(1, 6)]
print(l_c)
# é possivel colocar um / for / dentro do outro, apenas colocando eles em seguida.
# também é possivel colocar as condições, igual nos exemplos acima

STRINGS
'''
'''
print('---')
str = 'Otávio Miranda'
n_letras = 4
new_string = '.'.join([str[index:index + n_letras] for index in range(0, len(str), n_letras)])
print(new_string)
print('---')
------
nomes = ['luis', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [f'{newnomes[:-1]}{newnomes[-1].upper()}' for newnomes in nomes]
print(novos_nomes)

# estranho, mas é possivel abrir um fstrings pra tratar a string de dentro do LC. mt doido 
'''
