from random import randint
from time import sleep

def linha(n):
    print('-='*n)

def sorteia(lst):
    linha(20)
    for c in range(0,5):
        lst.append(randint(0,20))
    print('Sorteando 5 valores da lista: ', end='')
    for v in lst:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')

def somaPAR(lst):
    soma=0
    for n in lst:
        if n%2==0:
            soma += n
    print(f'Somando os valores pares de {lst} temos {soma}')
    linha(20)

numeros=[]
nm2= []
sorteia(numeros)
somaPAR(numeros)
sorteia(nm2)
somaPAR(nm2)
