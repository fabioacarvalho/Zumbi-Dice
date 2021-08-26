import random

dadoVerde = "CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"
dadoAmarelo = "TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"
dadoVermelho = "TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"
StartJogo = False

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
    inserirDados()
    #Adicionando jogadores:
    i = 1
    while (i < players + 1):
        pessoas = dict({'jogador': i, 'cerebros': 0, 'tiros': 0})
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
                    
                print(dados)

                #Pontuação do Jogo:
                print(f'Jogador {numJogador} comeu: ',jogadores[playerAtual]['cerebros'], 'cerebros.')
                print(f'Jogador {numJogador} levou: ',jogadores[playerAtual]['tiros'], 'tiros.')

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