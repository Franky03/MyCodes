from random import *
import time as tm
itens= ('Pedra', 'Papel', 'Tesoura')
comput= randint(0, 2)
print('''Escolhe ae:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
eu= int(input('Qual o Gon escolheria?'))
print('=='*15)
print('O computador escolheu {}'.format(itens[comput]))
print('Você jogou {}'.format(itens[eu]))
print('=='*15)
if comput==0: #Pedra
    if eu==0:
        print('EMPATE')
    elif eu==1:
        print('VC GANHOU')
    elif eu==2:
        print('VC PERDEU')
    else:
        print('Jogada inválida')
elif comput==1: #Papel
    if eu==0:
        print('VC PERDEU')
    elif eu==1:
        print('EMPATE')
    elif eu==2:
        print('VC GANHOU')
    else:
        print('Jogada inválida')
elif comput==2: #Tesoura
    if eu==0:
        print('VC GANHOU')
    elif eu==1:
        print('VC PERDEU')
    elif eu==2:
        print('EMPATE')
    else: 
        print('Jogada Inválida')
print('=='*15)