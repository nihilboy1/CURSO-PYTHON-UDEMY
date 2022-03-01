produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 41},
    {'nome': 'p3', 'preco': 24},
    {'nome': 'p4', 'preco': 55},
    {'nome': 'p5', 'preco': 51.9},
    {'nome': 'p6', 'preco': 41.70},
    {'nome': 'p7', 'preco': 10.90},
    {'nome': 'p8', 'preco': 98},
    {'nome': 'p9', 'preco': 12},
    {'nome': 'p10', 'preco': 444},
]

pessoas = [
    {'nome': 'luiz', 'idade': 22},
    {'nome': 'andre', 'idade': 12},
    {'nome': 'luigi', 'idade': 29},
    {'nome': 'lucas', 'idade': 28},
    {'nome': 'levi', 'idade': 27},
    {'nome': 'lazaro', 'idade': 26},
    {'nome': 'amaro', 'idade': 25},
    {'nome': 'pedro', 'idade': 24},
    {'nome': 'jeff', 'idade': 23},
    {'nome': 'kat', 'idade': 30},
]

lista = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def limpa(a):
    x = a.replace('.', '').replace('-', '').replace('/', '')
    return x


def validacnpj(a):
    a = limpa(a)
    cnpj_sem_digitos = a[:-2]  # 12 digitos
    numeros = []
    l1 = 5
    l2 = 9
    for digitos in cnpj_sem_digitos:
        if 5 >= l1 >= 2:
            numeros.append(int(digitos) * l1)
            l1 -= 1
        elif l2 < 10:
            numeros.append(int(digitos) * l2)
            l2 -= 1
    else:
        prime_digito = 11 - (sum(numeros) % 11)
        prime_digito = 0 if prime_digito > 9 else prime_digito
        cnpj_1 = cnpj_sem_digitos + str(prime_digito)
    numeros.clear()
    l1 = 6
    l2 = 9
    for c in cnpj_1:
        if 6 >= l1 >= 2:
            numeros.append(int(c) * l1)
            l1 -= 1
        elif l2 < 10:
            numeros.append(int(c) * l2)
            l2 -= 1
    else:
        segun_digito = 11 - (sum(numeros) % 11)
        segun_digito = 0 if segun_digito > 9 else segun_digito
        cnpjok = cnpj_1 + str(segun_digito)
    if cnpjok == a:
        return f'{cnpjok} É VÁLIDO!'
    else:
        return f'{cnpjok} É INVÁLIDO!'


