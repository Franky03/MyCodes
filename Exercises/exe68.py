import random
from time import sleep
cont=0
soma=0
escolha= ''
print('=='*15)
print('Par ou Impar')
print('=='*15)
while True:
    computador= random.randint(0,10)
    jogador= int(input('Digite um número: '))
    escolha= str(input('Par ou ímpar [P/I]')).strip().upper()
    soma= jogador + computador
    if escolha in 'Pp':
        if soma%2 ==0:
            sleep(1)
            print(f'Vc jogou o número {jogador} e o computador jogou {computador}')
            print ('Você acertou')
            cont +=1
        else:
            sleep(1)
            print(f'Vc jogou o número {jogador} e o computador jogou {computador}')
            print('Você perdeu')
            print(f'Seu recorde foi de {cont} vitória(s)')
            print('='*20)
            break
    elif escolha in 'Ii':
        if soma%2==1:
            sleep(1)
            print(f'Vc jogou o número {jogador} e o computador jogou {computador}')
            print('Vc acertou')
            cont+=1
        else:
            sleep(1)
            print(f'Vc jogou o número {jogador} e o computador jogou {computador}')
            print('Vc perdeu')
            print(f'Seu recorde foi de {cont} vitória(s)')
            print('='*20)
            break
