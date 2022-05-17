def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gols")

j= str(input('Nome do jogador: '))
g= str(input('Gols: '))
if g.isnumeric(): #Se o g for númerico,
    g= int(g)                        #  vai transformar g em inteiro
else:
    g=0 #Se ele não for númerico, ou seja, se não escrever g, ele vai valer 0
if j.strip()=='': #Se o nome do jogador, eliminando os espaços inúteis for vazio,
    ficha(gols=g)                                                              # a ficha vai ser só com gols
else:
    ficha(j,g) #Se não for vazio, a ficha vai ser com jogador e com gols
