"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

eu basicamente ensino a minha classe a fazer algo

Operador    Método Mágico   Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        w = self.x * self.y
        w2 = other.x * other.y
        return w * w2

    '''
    aqui eu posso também retornar um novo objeto de classe, 
    - por exemplo: return Retangulo(w,w2) 
    para criar de fato esse novo objeto, eu forço o meu código a entrar no __add__
    - por exemplo: r3 = r1 + r2
    '''

    def __lt__(self, other):
        print('batata')
        return self.x < other.x



    '''
    Nos métodos mágicos de sobrecarga de operadores, eu posso forçar a entrada 
    de duas instâncias dentro de uma função, se eu chamar ela através do operador necessário
    
    no caso acima, eu obriguei r1 e r2 a entrarem em __add__ quando chamei eles com o operador de +
    entretando, dentro da função em si, fiz uma conta de multiplicação
    '''


r1 = Retangulo(2, 2)
r2 = Retangulo(5, 1)
print(r1 < r2)
