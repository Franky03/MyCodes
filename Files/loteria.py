from random import *
lista=[]
jogos=[]
n=int(input('Quantos jogos quer sortear?: '))
contn=1
while contn<=n:
    cont=0
    while True:
        num= randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contn+=1
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
