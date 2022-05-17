primeiro_termo=int(input('Primeiro Termo: '))
razao= int(input('Razão: '))
termo= primeiro_termo
cont= 1
while cont<=10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont +=1