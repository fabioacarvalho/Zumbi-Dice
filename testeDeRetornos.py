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

play = True

if play == True:
    inserirDados()

cont = 0

while (play == True):
    dados = []
    for i in range(0, 3):
        oq = random.choice(random.choice(tubo))
        dados.append(oq)
        try: 
            if oq == "CEREBRO":
                cont += 1
                del tubo[i]

            if len(tubo) == 0:
                inserirDados()
            elif play == False:
                inserirDados()

        except:
            print("Preenchendo o tubo")
        
    print(f'ainda tem: {len(tubo)} dados')
    print(f'seus pontos: {cont}')
    print(f'------- {dados}')

    continuar = int(input('continuar no jogo [1] - SIM e [2] - NÃO'))
    if continuar == 2:
        play = False