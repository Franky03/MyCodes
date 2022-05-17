jogador={}
gols=list()
jogador['Nome']= str(input('Nome do Jogador: '))
partidas= int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
jogador['Gols']= gols
for c in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na {c+1}º partida? ')))
jogador['Total']= sum(gols)
print(jogador)
print('=-'*20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('=-'*20)
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.\n")
for i, v in enumerate(gols):
    print(f"   =>Na partida {i+1} ele fez {v} gols.")
print(f"Foi um total de {jogador['Total']} gols.")
print('=-'*20)