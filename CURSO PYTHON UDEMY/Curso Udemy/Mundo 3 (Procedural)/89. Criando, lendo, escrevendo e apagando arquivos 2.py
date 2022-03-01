import json

'''
try:
    file = open('abc2.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
'''

'''
o modo r apenas lê o que ja está escrito no arquivo
o modo a adiciona novos valores ao arquivo sem apagar os anteriores

with open('abc2.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 1\n')
    file.write('Linha 1\n')

    file.seek(0)
    print(file.read())
'''

d1 = {'Pessoa1':
          {'Nome': 'Luiz', 'Idade': 25, },
      'Pessoa2':
          {'Nome': 'Rose', 'Idade': 15}}

d1_json = json.dumps(d1)

with open('abc2.json', 'w+') as file:
    file.write(d1_json)
