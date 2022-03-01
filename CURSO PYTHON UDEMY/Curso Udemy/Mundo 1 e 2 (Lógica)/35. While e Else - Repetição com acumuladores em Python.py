contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador = contador + 1
else:
    print('Expressão tounou-se falsa!')
print('Fora!')

#o contador conta linearmente
#o acumulador guarda numeros de acordo com a contagem

#o else só é excecutado se o a condição do laço se tornar falsa