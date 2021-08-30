import random

dadoVerde = ["CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoAmarelo = ["TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoVermelho = ["TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"]
StartJogo = False

tubo = []

#Adicionar dados no copo
def inserirDados():
    for i in range(0, 6):
        tubo.append({"dadoVerde": dadoVerde})
    for i in range(0, 4):
        tubo.append({"dadoAmarelo": dadoAmarelo})
    for i in range(0, 3):
        tubo.append({"dadoVermelho": dadoVermelho})

#Rodada do jogo:
mao = []

def sorteio():
    mao.append(random.choice(tubo))


inserirDados()
sorteio()

print(mao)

for i in range(0, 1):
    print(mao[i])