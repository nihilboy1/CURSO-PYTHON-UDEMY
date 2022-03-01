from itertools import combinations, permutations, product


pessoas = ['luis', 'maria', 'joao', 'luiz', 'eduardo']
'''
for grupo in combinations(pessoas, 2):
    print(grupo)
'''
# com o combinations() a ordem do grupo formado não importa.
# se os valores ja tiverem sido usados, eles não se repetem
"""
for grupo in permutations(pessoas, 2):
    #print(grupo)
"""
# caso eu queira que todos os valores sejam mostrados, eu uso o permutations()
for grupo in product(pessoas, repeat=2):
    print(grupo)
# se eu quiser até mesmo repetir os valores base, eu chamo o product()
