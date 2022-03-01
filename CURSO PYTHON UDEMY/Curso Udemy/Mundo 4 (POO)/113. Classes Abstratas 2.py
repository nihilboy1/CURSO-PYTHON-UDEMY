from POUP113 import Conta_Poup
from CORREN113 import Conta_Corre
'''x = Conta() é uma chamada inviavel, pois a classe mãe é abstrata'''
a = Conta_Poup(1111, 2222, 500)
a.sacar(20)
a.depositar(500)
print('***************')

b = Conta_Corre(1234, 7777, 5000, 500)
b.sacar(49)
b.sacar(51)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)
b.sacar(500)