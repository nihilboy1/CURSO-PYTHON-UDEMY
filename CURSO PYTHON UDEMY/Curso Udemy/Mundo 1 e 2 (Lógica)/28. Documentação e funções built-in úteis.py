num1 = input('Digite algo: ')
num2 = input('Digite outra coisa: ')


try:
    print('kkk'.format(num3))
except:
    print('quebra')


#Essa função try serve basicamente como um if, entretanto, caso o código quebre dentro dela, ela não mostra mensagem de erro
#em vez disso, pula para o except