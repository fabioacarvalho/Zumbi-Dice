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

dadoVerde = ["CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoAmarelo = ["TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoVermelho = ["TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"]
StartJogo = True

tubo = []

#Adicionar dados no copo
def inserirDadosTubo():
    for i in range(0,6):
        tubo.append(dadoVerde)
    for i in range(0, 4):
        tubo.append((dadoAmarelo))
    for i in range(0, 3):
        tubo.append(dadoVermelho)

#Quantos jogadores estão jogando:
players = int(input("Quantos jogadores vão jogar: "))
jogadores = []

if players >= 2:
    StartJogo = True
    #Adicionando jogadores:
    i = 1
    while (i < players + 1):
        pessoas = dict({'jogador': i, 'cerebros': 0})
        jogadores.append(pessoas)
        i += 1
    
    print(jogadores)

    #Início do Jogo:
    while StartJogo == True:
        #Escolhas 1:
        numJogador = int(input("Qual jogador vai jogar os dados? [1, 2...]: "))
        
        print(f'Jogador: {numJogador}')
        #Início do jogo:
        turno = False
        if numJogador != 0:
            turno = True

        #Jogar os dados:
        dadosNoJogo = jogarDados
                    

        while (turno == True):

            #Escolhas 2:
            jogar = int(input("[1] - Jogar dados ou [2] - Finalizar Turno? "))

            #Estrutura de pontos por jogador:
            if jogar == 1:
                
                if jogarDados[0:3] == "TIRO":
                    print('Você foi atingido por 3 tiros e perdeu o turno!')
                if jogarDados[0] == "CEREBRO":
                    jogadores[numJogador - 1]['cerebros'] += 1
                if jogarDados[1] == "CEREBRO":
                    jogadores[numJogador - 1]['cerebros'] += 1
                if jogarDados[2] == "CEREBRO":
                    jogadores[numJogador - 1]['cerebros'] += 1
                    
               
                print(jogarDados)
                print(jogadores[numJogador - 1]['cerebros'])

            elif jogar == 2:
                print("Seu turno finalizou, proximo jogador")
                turno = False
        
        #Continuar ou sair do jogo:
        contiuar = int(input("Continuar jogo [1]-SIM e [2]-NÃO: "))
        if contiuar == 2:
            StartJogo = False
        
        


elif players < 2:
    print("jogadores insuficiente, chame mais amigos para jogar...")