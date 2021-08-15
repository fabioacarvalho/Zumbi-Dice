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
StartJogo = False

tubo = []
copo = 13

#Adicionar dados no copo
for i in range(0,6):
    tubo.append(dadoVerde)
for i in range(0, 4):
    tubo.append((dadoAmarelo))
for i in range(0, 3):
    tubo.append(dadoVermelho)

#Sortear dados:
DadosUm = random.choice(random.choice(tubo))
DadosDois = random.choice(random.choice(tubo))
DadosTres = random.choice(random.choice(tubo))


#Jogar 3 dados:
jogarDados = [DadosUm, DadosDois, DadosTres]

#print(jogarDados)

#Quantos jogadores estão jogando:
players = int(input("Quantos jogadores vão jogar: "))
jogadores = []

if players >= 2:
    #Início do jogo:
    StartJogo = True
    
    #Adicionando jogadores:
    i = 1
    while (i < players + 1):
        pessoas = dict({'jogador': i, 'cerebros': 0})
        jogadores.append(pessoas)
        i += 1

    #Escolhas:
    numJogador = int(input("Qual jogador vai primeiro [1, 2, 3...]: "))
    jogar = int(input("[1] - Jogar dados ou [2] - Finalizar Turno? "))

    if jogar == 1:
        
        valores = jogarDados
        if valores[0:2] == "TIRO":
            print('Você foi atingido por 3 tiros e perdeu o turno!')
        if valores[0] == "CEREBRO":
            jogadores[numJogador]['cerebros'] += 1
        if valores[1] == "CEREBRO":
            jogadores[numJogador]['cerebros'] += 1
        if valores[2] == "CEREBRO":
            jogadores[numJogador]['cerebros'] += 1


        print(valores)
        print(jogadores[numJogador]['cerebros'])
    elif jogar == 2:
        print("Seu turno finalizou, proximo jogador")


elif players < 2:
    print("jogadores insuficiente, chame mais amigos para jogar...")