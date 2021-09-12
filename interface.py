from design.designJogo import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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

#Quantos jogadores estão jogando:
jogadores = []

#Variavel de controle de inicio:
if StartJogo == True:
    inserirDados()

cont = 0



class Jogo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        

        ## PAGES JOGO

        self.btnSair.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btnJogar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btnIniciar.clicked.connect(self.jogo)

        #Botões:
        
    def getItem(self, listaJogadores):
        #print(self.current().text())
        jogad = listaJogadores.text()
        print(jogad)
        #print(self.currentRow())
    

    def sorteio():
        for i in range(0, 3):
            mao.append(random.choice(tubo))

    def jogo(self):
        players = int(self.numJogadores.text())

        
        if players >= 2:
            self.stackedWidget.setCurrentWidget(self.page_3)

            #Início do jogo:
            StartJogo = True
            inserirDados()
            #Adicionando jogadores:
            i = 1
            while (i < players + 1):
                pessoas = dict({'jogador': i, 'cerebros': 0, 'tiros': 0})
                jogadores.append(pessoas)
                i += 1

            for i in jogadores:
                self.listaJogadores.addItem(f'Jogador: {i}')
    
            
            
            #self.itemDoubleClicked.connect(self.getItem)

            self.listaJogadores.itemDoubleClicked.connect(self.getItem)

            """
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
                        if jogadores[playerAtual]['tiros'] == 3:
                            turno = False
                            print(f'Você levou 3 tiros e perdeu o turno.')
                            jogadores[playerAtual]['tiros'] = 0
                            break
                        else:
                            jogar = int(input("[1] - Jogar dados ou [2] - Finalizar Turno? "))
                    except:
                        print("Valor inválido!")
                    try:
                        if jogar == 1:
                            #Jogando os dados:    
                            dados = []
                            
                            sorteio()

                            #Adicionando Pontos nova etapa:
                            #Cores e faces dos dados:
                            for i in range(0, 3):
                                
                                if "dadoVermelho" in mao[i]:
                                    dadoFace = random.choice(mao[i]["dadoVermelho"])
                                    print(f"Dado Vermelho: {dadoFace}")  
                                if "dadoVerde" in mao[i]:
                                    dadoFace = random.choice(mao[i]["dadoVerde"])
                                    print(f"Dado Verde: {dadoFace}")
                                if "dadoAmarelo" in mao[i]:
                                    dadoFace = random.choice(mao[i]["dadoAmarelo"])
                                    print(f"Dado Amarelo: {dadoFace}")
                                try:
                                    if dadoFace == "CEREBRO":
                                        if jogadores[playerAtual]['cerebros'] == 13:
                                            print(f'PARABÉNS o jogador {numJogador} venceu!')
                                            turno = False
                                            StartJogo == False
                                        else:
                                            jogadores[playerAtual]['cerebros'] += 1
                                    elif dadoFace == "TIRO":
                                        if jogadores[playerAtual]['tiros'] == 3:
                                            turno = False
                                            print(f'Você levou 3 tiros e perdeu o turno.')
                                            jogadores[playerAtual]['tiros'] = 0
                                            break
                                        else:
                                            jogadores[playerAtual]['tiros'] += 1
                                    
                                    
                                    del mao[i]
                                    if len(tubo) == 0:
                                        inserirDados()
                                    elif StartJogo == False:
                                        inserirDados()
                                    elif len(mao) < 3:
                                        sorteio()
                                except:
                                    print("Preenchendo o tubo")   

                            #Pontuação do Jogo:
                            print(f'Jogador {numJogador} comeu: ',jogadores[playerAtual]['cerebros'], 'cerebros.')
                            print(f'Jogador {numJogador} levou: ',jogadores[playerAtual]['tiros'], 'tiros.')

                        elif jogar == 2:
                            print("Seu turno finalizou, proximo jogador")
                            turno = False
                            jogadores[playerAtual]['tiros'] = 0
                    except:
                        print("Valor invalido!!")

            try:
                continuar = int(input('continuar o jogo [1] - SIM e [2] - NÃO: '))
                if continuar == 2:
                    StartJogo = False
            except:
                print("Valor inválido!")

        """

            

        elif players < 2:
            self.infoInicio.setText('Jogadores insuficiente, chame seus amigos...')
              

    



if __name__ == "__main__":
    qt = QApplication(sys.argv)
    novo = Jogo()
    novo.show()
    qt.exec_()