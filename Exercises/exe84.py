from re import TEMPLATE


temp=[]
pessoas=[]
cont=0
maior= menor=0
while True:
    nome= str(input('Nome: '))
    peso= float(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    if len(pessoas)==0:
        maior = menor = temp[1]
    else:
        if temp[1]> maior:
            maior=temp[1]
        if temp[1]< menor:
            menor=temp[1]
    pessoas.append(temp[:])
    temp.clear()
    opc=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opc in 'Nn':
        break
print('=-'*20)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso é {maior} ', end= '')
for p in pessoas:
    if p[1]== maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso é {menor} ', end='')
for b in pessoas:
    if b[1]== menor:
        print(f'[{b[0]}] ', end='')