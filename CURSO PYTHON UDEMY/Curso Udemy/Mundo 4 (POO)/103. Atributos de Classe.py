class A:
    v = 123


a1 = A()
print(a1.v)
print(A.v)
'''
Eu posso mostrar uma variavel de classe tanto através de uma instância,
quanto da própria classe
'''
A.v = 5
print(A.v)
print(a1.v)
'''
Se eu alterar o valor da variavel de classe através da classe, nas próximas
vezes que ela for chamada, ela tera o novo valor
'''
a1.v = 74
print(a1.v)
print(A.v)
'''
Contudo, se eu alterar o valor da variavel através da instancia, ele só é alterado localmente
'''










