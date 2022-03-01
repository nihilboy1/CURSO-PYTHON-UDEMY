def esprint(txt):
    c = len(txt) + 2
    print('-' * c)
    print(f'{txt}'.center(c, ' '))
    print('-' * c)


texto = str(input('Escreva algo: '))
esprint(texto)
