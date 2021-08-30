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
    #for i in range(0, 3):
    


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
                    #Etapa ANTIGA:
                    #facesDados = random.choice(random.choice(tubo))
                    #dados.append(facesDados)
                    #FIM ETAPA.

                    sorteio()


                    #Adicionando Pontos nova etapa:
                    #Cores e faces dos dados:
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