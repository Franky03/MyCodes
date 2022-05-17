#Aqui não sei como fazer no VSCode, o cara estava usando no pycharme

np= int(input('Digite um número: '))
for c in range(1,np+1):
    if np%c==0:
        print('Divisível', end='')
    else:
        print('N divisível', end='')
print('{}'.format(c), end=' ')