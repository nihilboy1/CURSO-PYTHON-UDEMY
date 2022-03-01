
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [(v, v2) for v in l1 for v2 in range(3)]
# print(ex1)


l2 = ['luiz', 'mauro', 'maria']
ex2 = [v.replace('a', '@') for v in l2]
# print(ex2)


tup = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
)
ex4 = [(y, x) for x, y in tup]
# print(ex4)


l3 = list(range(100))
ex5 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# print(ex5)

ex6 = [v if v % 3 == 0 else 'X' for v in l3]
print(ex6)


