time= list()
jogador= dict()
gols= list()
while True:
    # Apagar gols e jogador pra adicionar outro
    gols.clear() 
    jogador.clear()
    ##
    jogador['Nome']= str(input('Nome do Jogador: '))
    partidas= int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na {c+1}º partida? ')))
    jogador['Gols']= gols[:] #Cópia da lista gols, se não for a cópia vai dar erro lá na frente
    jogador['Total']= sum(gols)
    time.append(jogador.copy()) #Cópia do dicionário jogador
    while True:
        conti= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if conti in 'SsNn':
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if conti in 'Nn':
        break
print('=-'*20)
print('cod ', end='')
for i in jogador.keys(): #Colocar as chaves em cima da tabela
    print(f'{i:<15}', end='')
print()
print('--'*20)
for k, v in enumerate(time): #Mostrar o index, nome, gols e o total da lista/dicionário
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca= int(input("Mostrar dados de qual jogador? [100 para parar]: "))
    if busca==100:
        break
    if busca>= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f"---- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']} ----")
        for i, g in enumerate(time[busca]['Gols']): #Mostrar os gols separadamente
            print(f"   No jogo {i+1} fez {g} gols")
    print('--'*20)
print("FIM")