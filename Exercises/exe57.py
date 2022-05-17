'''s= str(input('Sexo[M/F]: ')).strip().upper()[0]
while s not in 'MmFf':
    s= str(input('Dados errados. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(s))'''
import random as rd

pc= rd.randint(0, 10)
acertou= False
palpites=0
print('Vou escolher um número de 0 a 10...')
while not acertou:
    eu= int(input('Qual seu palpite? '))
    palpites += 1
    if eu==pc:
        acertou= True
    else:
        if eu<pc:
            print('Mais... Tente de novo: ')
        else:
            print('Menos...Tente de novo: ')
print('Acertou com {} tentativas'.format(palpites))