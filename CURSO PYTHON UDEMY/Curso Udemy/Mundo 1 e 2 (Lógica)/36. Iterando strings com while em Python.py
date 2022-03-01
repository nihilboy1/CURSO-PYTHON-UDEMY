#       'indices'
#       '0123456789
# valores que contem indices são chamados de valores iteraveis
frase = 'o rato roeu a roupa do rei de roma'
tam = len(frase)
some = str(input('Qual letra quer transformar em Maiusculo: '))
c = 0
nova_palavra = ''
while c < tam:
    letra = frase[c]
    if letra == some:
        nova_palavra = nova_palavra + some.upper()
    else:
        nova_palavra = nova_palavra + letra
    c = c + 1
print(nova_palavra)
