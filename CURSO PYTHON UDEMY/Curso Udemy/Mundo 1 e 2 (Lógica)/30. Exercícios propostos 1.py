num = (input('Digite um numero INTEIRO: '))
print('Valor informado: {}'.format(num))
if num.isdigit():
    num = int(num)
    divi = num % 2
    if divi == 1:
        print('O numero informado é impar!')
    else:
        print('O numero informado é par')
else:
    print('Você não informou um numero INTEIRO!')



