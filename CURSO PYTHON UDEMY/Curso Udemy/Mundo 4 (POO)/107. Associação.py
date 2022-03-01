from ASSOCIACAO107 import Escritor, Caneta, Maquina_de_escrever

'''
Composição é quando uma classe usa a outra
'''

escritor = Escritor('João')
caneta = Caneta('Bic')
'''
aqui, a instância "caneta" recebe os métodos da classe "Caneta()"
'''
maquina = Maquina_de_escrever()

maquina.escrever()
caneta.escrever()
print(escritor.nome)
print(caneta.marca)
escritor.ferramenta = caneta
'''
Aqui, a variavel "ferramenta", que está dentro da instância "escritor" 
recebe a instância "caneta", ques está guardando a classe "Caneta()"
'''
escritor.ferramenta.escrever()
'''
aqui eu chamo a função "escrever()" atraves do local onde eu armazenei os métodos de "caneta"
'''
