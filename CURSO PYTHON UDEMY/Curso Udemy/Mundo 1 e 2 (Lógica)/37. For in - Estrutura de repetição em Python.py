"""
for in em python
iterando strings com for
função range(start=0, stop, step=1)


"""
"""
texto = 'python'

for cada_item in texto:
    print(cada_item)
#usando o for, eu consigo usar a própria string como condição de parada do laço.
#o for identifica a quantidade de itens no index e executa o código até que chegue no limite imposto por ele 
"""
"""
texto = 'python'

for cada_item in range(1, 21, 1):
    print(cada_item)
#o inicio em 0 e o step em 1 são o padrão.
#caso eu queira fazer uma contagem decrescente, eu coloco o inicio maior que o fim e no step, informo com -1
"""


texto = 'python'
palavranova = ''
for cada_item in texto:
    if cada_item == 'n':
        palavranova = palavranova + 'N'
    elif cada_item == 'y':
        palavranova = palavranova + 'Y'
    else:
        palavranova = palavranova + cada_item
print(palavranova)

