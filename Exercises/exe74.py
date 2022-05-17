from random import *
tupla=(randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
'''sortt=sorted(tupla)
menor= sortt[0]
maior= sortt[-1]'''
print(f'\nO menor valor da tupla é {min(tupla)}')
print(f'O maior valor da tupla é {max(tupla)}')
