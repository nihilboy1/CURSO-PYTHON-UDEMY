def converte_numero(v):
    try:
        v = int(v)
        return v
    except Exception:
        try:
            v = float(v)
            return v
        except Exception:
            pass
while True:
    num = converte_numero(input('Digite um número: '))
    if num is not None:
        print(num * 00.577)
    else:
        print('Entrada inválida!')

#código mt importante pra n quebrar códigos
