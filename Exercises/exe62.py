primeiro_termo=int(input('Primeiro Termo: '))
razao= int(input('Razão: '))
termo= primeiro_termo
cont= 1
total=0
mais=10
while mais !=0:
    total+=mais
    while cont<=total:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont +=1
    print('PAUSA')
    mais= int(input('Quantos termos vc quer mostrar a mais? '))
print('FIM')
print('O total de progressão foi de {}'.format(total))