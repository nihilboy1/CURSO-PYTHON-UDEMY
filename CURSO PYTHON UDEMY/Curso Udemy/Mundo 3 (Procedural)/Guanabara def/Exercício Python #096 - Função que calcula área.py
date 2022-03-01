def area(larg, alt):
    quad = larg * alt
    print('Medidor de área quadrada')
    print('A área de um terreno de {} x {} é de {}m²'.format(larg, alt, quad))


a1 = float(input('Informe a largura do terreno: '))
a2 = float(input('Informe o comprimento do terreno: '))
area(a1, a2)

