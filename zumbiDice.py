''' 
    NOME: FÁBIO ALEX DE CARVALHO
    CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
 '''

import random

dadoVerde = ["CEREBRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoAmarelo = ["TIRO","PASSO","CEREBRO","TIRO","PASSO","CEREBRO"]
dadoVermelho = ["TIRO","PASSO","TIRO","CEREBRO","PASSO","TIRO"]
StartJogo = False
tubo = []
cerebrosTurno = [{"cerebros": 0}]

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
maoPasso = []
def lancarDados(valor):
    if len(valor) < 3:
        valTubo = 3 - len(valor)
        for i in range(0, valTubo):
            valor.append(random.choice(tubo))

#FUNÇÃO PARA PONTUAÇÃO:
def pontuacao(valor):
    for i in range(0, 3):
        if "dadoVermelho" in valor[i]:
            dadoFace = random.choice(valor[i]["dadoVermelho"])
            print(f"Dado Vermelho: {dadoFace}")  
            print('')
        if "dadoVerde" in valor[i]:
            dadoFace = random.choice(valor[i]["dadoVerde"])
            print(f"Dado Verde: {dadoFace}")
            print('')
        if "dadoAmarelo" in valor[i]:
            dadoFace = random.choice(valor[i]["dadoAmarelo"])
            print(f"Dado Amarelo: {dadoFace}")
            print('')
        try:
            if dadoFace == "CEREBRO":
                if jogadores[playerAtual]['cerebros'] == 13:
                    print(f'PARABÉNS o jogador {numJogador} venceu!')
                    turno = False
                    StartJogo == False
                else:
                    jogadores[playerAtual]['cerebros'] += 1
                    cerebrosTurno[0]['cerebros'] += 1
            elif dadoFace == "TIRO":
                if jogadores[playerAtual]['tiros'] == 3:
                    turno = False
                    print(f'Você levou 3 tiros e perdeu o turno.')
                    print('')
                    print(cerebrosTurno)
                    print('')
                    jogadores[playerAtual]['tiros'] = 0
                    jogadores[playerAtual]['cerebros'] -= cerebrosTurno[0]['cerebros']
                    cerebrosTurno[0]['cerebros'] = 0
                    break
                else:
                    jogadores[playerAtual]['tiros'] += 1
            elif dadoFace == "PASSO":
                maoPasso.append(valor[i])
            del mao[i]
            if len(tubo) == 0:
                inserirDados()
            elif StartJogo == False:
                inserirDados()
            elif len(valor) < 3:
                lancarDados(valor)
        except:
            print("Preenchendo o tubo")

#Iniciando o Jogo e perguntando quantos jogadores estão jogando:
print('')
print('---------SEJAM BEM VINDOS AO ZUMBI DICE ---------')
print('')
players = int(input("Quantos jogadores vão jogar: "))
jogadores = []
def listarJogadores():
    for i in jogadores:
        print(f"Jogador nº {i['jogador']} - Pontuação: {i['cerebros']}")

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
            print('')
            print(f"Qual dos jogadores abaixo vai jogar os dados? ")
            listarJogadores()
            print('')
            numJogador = int(input("Digite o número do jogador: "))
            print('')
            playerAtual = numJogador - 1
        except:
            print("Valor inválido!")
            break
        turno = False
        if numJogador != 0:
            turno = True
        while (turno == True):
            #MENU
            def menu():
                print('')
                print('---------------------- MENU ----------------------')
                print('')
                print(f'Jogador nº {playerAtual + 1} com os dados, o que deseja fazer?')
                print('')
                print('1 - Jogar Dados:')
                print('2 - Finalizar Turno:')
                print('3 - Listar Pontução:')
                print('')
                valor = int(input('Escolha uma opção: '))
                if valor == 1:
                    jogar = 1
                    return jogar
                elif valor == 2:
                    jogar = 2
                    return jogar
                elif valor == 3:
                    print('')
                    print('-------------- LISTA DE PONTUAÇÃO --------------')
                    print('')
                    listarJogadores()
                    menu()
                else:
                    print('Valor inválido!')

            #Jogar dados ou sair do turno:
            try:
                if jogadores[playerAtual]['tiros'] == 3:
                    turno = False
                    print(f'Você levou 3 tiros e perdeu o turno.')
                    jogadores[playerAtual]['tiros'] = 0
                    jogadores[playerAtual]['cerebros'] -= cerebrosTurno[0]['cerebros']
                    cerebrosTurno[0]['cerebros'] = 0
                    break
                elif jogadores[playerAtual]['cerebros'] >= 13:
                    print(f'PARABÉNS o jogador {numJogador} venceu!')
                    turno = False
                    StartJogo == False
                    break
                else:
                    jogar = menu()
            except:
                print("Valor inválido!")
            try:
                if jogar == 1:
                    #Jogando os dados:    
                    dados = []
                    lancarDados(mao)

                    #Adicionando Pontos nova etapa - Cores e faces dos dados:
                    pontuacao(mao)
                    
                    if len(maoPasso) >= 1:
                        irAtras = int(input('Deseja ir atrás dos passos [1] - SIM / [2] - NÃO: '))
                        if irAtras == 1:
                            lancarDados(maoPasso)
                            pontuacao(mao)
                        maoPasso.clear()

                    #Pontuação do Jogo:
                    print(f'Jogador {numJogador} comeu: ',jogadores[playerAtual]['cerebros'], 'cerebros.')
                    print(f'Jogador {numJogador} levou: ',jogadores[playerAtual]['tiros'], 'tiros.')
                elif jogar == 2:
                    print('')
                    print(f"Seu turno finalizou jogador {playerAtual + 1}, proximo jogador")
                    turno = False
                    jogadores[playerAtual]['tiros'] = 0
            except:
                print("Valor invalido!!")
        try:
            if jogadores[playerAtual]['cerebros'] < 13:
                print('')
                continuar = int(input('continuar o jogo [1] - SIM e [2] - NÃO: '))
            elif jogadores[playerAtual]['cerebros'] >= 13:
                break
            if continuar == 2:
                StartJogo = False
        except:
            print("Valor inválido!")
elif players < 2:
    print("jogadores insuficiente, chame mais amigos para jogar...")
