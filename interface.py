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
        print(listaJogadores.text())
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
                self.listaJogadores.addItem(f'jogador: {i}')

            
            
            #self.itemDoubleClicked.connect(self.getItem)

            self.listaJogadores.itemDoubleClicked.connect(self.getItem)
            
        
            

            

            

        elif players < 2:
            self.infoInicio.setText('Jogadores insuficiente, chame seus amigos...')
              

    



if __name__ == "__main__":
    qt = QApplication(sys.argv)
    novo = Jogo()
    novo.show()
    qt.exec_()