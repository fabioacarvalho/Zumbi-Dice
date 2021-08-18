import random

dadoVerde = "CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"
dadoAmarelo = "TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"
dadoVermelho = "TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"
StartJogo = True

tubo = []

#Adicionar dados no copo
def inserirDados():
    for i in range(0,6):
        tubo.append(dadoVerde)
    for i in range(0, 4):
        tubo.append((dadoAmarelo))
    for i in range(0, 3):
        tubo.append(dadoVermelho)

print(tubo)


inserirDados()

print(tubo)
