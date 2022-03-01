from CLASSES98 import Pessoa, Pessoas1
'''
Quando eu estiver criando uma classe, eu devo entender ela realmente como um objeto real 
capaz de executar ações, dai depois eu transformo isso em código
'''
a = Pessoa()
a.falar()
'''
Eu crio uma classe, e depois os atributos da classe. 
depois eu posso abribuir a classe à uma variavel, e depois chamar os atributos da classe como metodos da variavel
'''

bo = Pessoas1('Bolsonaro', 66)
lu = Pessoas1('Lula', 76)
print(bo.nome)
'''
Aqui, por exemplo, quando eu chamo "b.nome", eu me refiro ao paramentro "nome" da classe
'''
bo.outro_metodo()
'''
aqui eu to chamando a variavel que foi atribuida no método acima, para o metodo de baixo
'''
bo.comer('uva')  # Bolsonaro está comendo um(a) uva
bo.falar('POO')  # Bolsonaro não pode falar comendo...
bo.parar_de_comer()  # Bolsonaro parou de comer!
bo.parar_de_comer()  # Bolsonaro não está comendo!
bo.falar('POO')  # Bolsonaro está falando POO
bo.falar('POO')  # Bolsonaro já está falando...
lu.falar('bolinho')  # Lula está falando bolinho
bo.comer('uva')  # Bolsonaro não consegue comer falando
bo.parar_de_falar()  # Bolsonaro parou de falar!
bo.comer('uva')  # Bolsonaro está comendo um(a) uva
bo.comer('uva')  # Bolsonaro já comeu!
bo.parar_de_comer()  # Bolsonaro parou de comer!
bo.falar('POO')  # Bolsonaro está falando POO

'''
as variaveis são independentes. se uma não pode, a outra talvez possa
'''

print(bo.anoatual)
print(bo.get_ano_de_nasc())
'''
aqui eu to usando uma variavel fixa e uma variavel da instancia pra fazer uma conta
'''
