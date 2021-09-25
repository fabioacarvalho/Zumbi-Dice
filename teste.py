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