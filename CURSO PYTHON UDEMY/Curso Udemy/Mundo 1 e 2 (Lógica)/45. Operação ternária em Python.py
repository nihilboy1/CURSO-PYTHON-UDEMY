"""
Operadores ternários
"""
lgdusr = True
msg = 'Logado!' if lgdusr else 'Aguardando login!'
print(msg)
# ----------------
idade = 18
maior = (idade >= 18)
# com esse teste, a variavel / maior / recebe True
if maior:
    print(idade)
