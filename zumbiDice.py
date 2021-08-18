"""
Assim, você deverá criar os dados neste momento utilizando um objeto do tipo string.
Esta string deve conter seis caracteres para simular cada face do dado.
Para identificar as faces dos dados segue abaixo especificação:

#6 Dados verdes: “CPCTPC”
#4 Dados amarelos: “TPCTPC”
#3 Dados vermelhos: “TPTCPT”

Onde, o caractere “C” na string corresponde ao cérebro, caractere “P” são os passos e por fim o “T” é o tiro.
"""

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


#Quantos jogadores estão jogando:
players = int(input("Quantos jogadores vão jogar: "))
jogadores = []

#Variavel de controle de inicio:
if StartJogo == True:
    inserirDados()

cont = 0


if players >= 2:
    #Início do jogo:
    StartJogo = True
    #Adicionando jogadores:
    i = 1
    while (i < players + 1):
        pessoas = dict({'jogador': i, 'cerebros': 0})
        jogadores.append(pessoas)
        i += 1

    

    while (StartJogo == True):

        #Escolhas:
        try:
            numJogador = int(input("Qual jogador vai jogar os dados? [1, 2...]: "))
            playerAtual = numJogador - 1
        except:
            print("Valor inválido!")
        

        turno = False
        if numJogador != 0:
            turno = True
        
        while (turno == True):
            #Jogar dados ou sair do turno:
            try:
                jogar = int(input("[1] - Jogar dados ou [2] - Finalizar Turno? "))
            except:
                print("Valor inválido!")

            if jogar == 1:
                #Jogando os dados:    
                dados = []
                for i in range(0, 3):
                    facesDados = random.choice(random.choice(tubo))
                    dados.append(facesDados)
                    #Adicionando pontos:
                    try: 
                        if facesDados == "CEREBRO":
                            if jogadores[playerAtual]['cerebros'] == 13:
                                print(f'PARABÉNS o jogador {numJogador} venceu!')
                                turno = False
                                StartJogo == False
                            else:
                                jogadores[playerAtual]['cerebros'] += 1
                        del tubo[i]
                        if len(tubo) == 0:
                            inserirDados()
                        elif StartJogo == False:
                            inserirDados()
                    except:
                        print("Preenchendo o tubo")
                    
                print(dados)

                #Pontuação do Jogo:
                print(f'Jogador {numJogador}: ',jogadores[playerAtual]['cerebros'])

            elif jogar == 2:
                print("Seu turno finalizou, proximo jogador")
                turno = False

        try:
            continuar = int(input('continuar o jogo [1] - SIM e [2] - NÃO'))
            if continuar == 2:
                StartJogo = False
        except:
            print("Valor inválido!")

    
elif players < 2:
    print("jogadores insuficiente, chame mais amigos para jogar...")