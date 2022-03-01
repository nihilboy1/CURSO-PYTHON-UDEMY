def voto(ano):
    from datetime import date
    atual = date.today().year
    id = atual - ano
    if 18 <= id < 65:
        return 'Idade: {} | Voto obrigatório!'.format(id)
    elif id < 16:
        return 'Idade: {} | Sem direito a voto'.format(id)
    elif id >= 16 or id >= 65:
        return 'Idade: {} | Voto opcional!'.format(id)

nasc = int()
print(voto(1998))
