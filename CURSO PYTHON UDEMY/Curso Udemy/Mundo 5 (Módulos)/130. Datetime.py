from datetime import datetime, timedelta

data = datetime(2021, 12, 22, 18, 55, 20)
'''
Essa classe "datetime" recebe os parametros na ordem: Ano, mês, dia, hora, minuto e segundo
'''
print(data)
'''
Printando do jeito que ta acima, ele sai no padrão americano
'''
print(data.strftime('%d/%m/%Y %H:%M:%S'))
'''
Com esse método ".strftime" eu consigo formatar o jeito que a informação vai sair
por exemplo, ajustando pra o padrão BR
tem mais métodos desses na documentação do módulo
'''
data2 = datetime.strptime('14/10/1998', '%d/%m/%Y')
print(data2)
'''
Com esse outro método eu consigo informa ja a data formatada, e depois informar o formato que eu informei
dai eu crio ja o objeto certinho na memória
'''
print(data2.timestamp())
'''
Esse ".timestamp" é a contagem de segundos até a data x que está na instância
'''
data2 = datetime.fromtimestamp(908334000.0)
print(data2)
'''
Também é possivel encontrar uma data a partir de um "timestamp"
'''
data2 = datetime.strptime('14/10/1998', '%d/%m/%Y')
data2 = data2 + timedelta(hours=5, seconds=2*30)
'''
com esse "timedelta" eu consigo adicionar um tempo x a uma data ja existente
'''

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('02/04/1957 20:00:00', '%d/%m/%Y %H:%M:%S')
dif = d1 - d2
print(dif.days)
'''
Eu também posso especificar mais esse print da diferença entre as datas usando métodos como
.seconds ou .totalseconds ou .days
'''

