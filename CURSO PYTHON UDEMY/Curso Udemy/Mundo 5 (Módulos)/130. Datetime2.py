from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')
'''
com a função "setlocale" eu consigo demostrar minha localização pro python,
e dai ele seta a formatação correta da data
'''
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
dt.strftime('%A, %d de %B de %Y')
dt2 = datetime.now().strftime('%d/%m/%Y')
print(dt)
print(dt2)
print(mes_atual, mdays[mes_atual])
'''
com o método ".now()" eu pego a data atual
'''
