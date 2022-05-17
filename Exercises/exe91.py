from random import *
from time import sleep
from operator import itemgetter
dados= {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3': randint(1,6),'Jogador4': randint(1,6)}
ranking= list()
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking= sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}.')
    sleep(1)