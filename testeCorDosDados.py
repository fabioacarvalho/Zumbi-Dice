import random

dadoVerde = ["CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoAmarelo = ["TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoVermelho = ["TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"]

tubo = []

#ADD TUBO:
def inserData():
    for i in range(0, 6):
        tubo.append({"dadoVerde": dadoVerde})
    for i in range(0, 4):
        tubo.append({"dadoAmarelo": dadoAmarelo})
    for i in range(0, 3):
        tubo.append({"dadoVermelho": dadoVermelho})

mao = []
faces = []

def sorteio():
    for i in range(0, 3):
        mao.append(random.choice(tubo))
    for i in range(0, 3):
        for i in mao:
            corDado = 
        

inserData()
sorteio()
print(faces)
print(len(faces))


#Adicionar dados no copo
def inserirDados():
    for i in range(0,6):
        tubo.append(dadoVerde)
    for i in range(0, 4):
        tubo.append((dadoAmarelo))
    for i in range(0, 3):
        tubo.append(dadoVermelho)
