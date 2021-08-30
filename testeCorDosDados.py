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

def sorteio():
    for i in range(0, 3):
        mao.append(random.choice(tubo))

inserData()
sorteio()

for i in range(0, 3):
    if "dadoVermelho" in mao[i]:
        dadoFace = random.choice(mao[i]["dadoVermelho"])
        print('Dado Vermelho')
        print(dadoFace)
    if "dadoVerde" in mao[i]:
        dadoFace = random.choice(mao[i]["dadoVerde"])
        print("Dado Verde.")
        print(dadoFace)
    if "dadoAmarelo" in mao[i]:
        dadoFace = random.choice(mao[i]["dadoAmarelo"])
        print("Dado Amarelo.")
        print(dadoFace)



print(len(mao))


#PONTOS DO JOGO NOVO:

                            try:
                                if dadoFace == "CEREBRO":
                                    if jogadores[playerAtual]['cerebros'] == 13:
                                        print(f'PARABÉNS o jogador {numJogador} venceu!')
                                        turno = False
                                        StartJogo == False
                                    else:
                                        jogadores[playerAtual]['cerebros'] += 1
                                elif dadoFace == "TIRO":
                                    if jogadores[playerAtual]['tiros'] >= 3:
                                        print(f'Você levou 3 tiros e perdeu o turno.')
                                        turno = False
                                        jogadores[playerAtual]['tiros'] = 0
                                    else:
                                        jogadores[playerAtual]['tiros'] += 1
                                del tubo[i]
                                if len(tubo) == 0:
                                    inserirDados()
                                elif StartJogo == False:
                                    inserirDados()
                            except:
                                print("Preenchendo o tubo")


#JOGO ANTERIOR:
#Adicionando pontos:
                    try: 
                        if facesDados == "CEREBRO":
                            if jogadores[playerAtual]['cerebros'] == 13:
                                print(f'PARABÉNS o jogador {numJogador} venceu!')
                                turno = False
                                StartJogo == False
                            else:
                                jogadores[playerAtual]['cerebros'] += 1
                        elif facesDados == "TIRO":
                            if jogadores[playerAtual]['tiros'] >= 3:
                                print(f'Você levou 3 tiros e perdeu o turno.')
                                turno = False
                                jogadores[playerAtual]['tiros'] = 0
                            else:
                                jogadores[playerAtual]['tiros'] += 1
                        del tubo[i]
                        if len(tubo) == 0:
                            inserirDados()
                        elif StartJogo == False:
                            inserirDados()
                    except:
                        print("Preenchendo o tubo")