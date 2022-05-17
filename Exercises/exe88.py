import random
import time

print('MEGA SENA')
print('=-'*30)
jogo=[]
lista=[]
n= int(input('Quantos jogos quer que sorteie ? :'))
contn=1
time.sleep(1)
while contn<=n:
    cont=0
    while True:
        num= random.randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont +=1
        if cont>=6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    contn+=1
print('=='*3, f'SORTEANDO {n} JOGOS', '=='*3)
time.sleep(1)
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print('-='*5, '<BOA SORTE>','-='*5)
