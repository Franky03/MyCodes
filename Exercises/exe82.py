lista=[]
pares=[]
impares=[]
while True:
    n=int(input('Digite um valor: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    elif n%2==1:
        impares.append(n)
    resp=str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=='*25)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
print('=='*25)