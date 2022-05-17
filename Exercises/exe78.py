lista= list()
maior=0
menor=0
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c==0:
        maior=menor=lista[c]
    else:
        if lista[c]>maior:
            maior=lista[c]
        if lista[c]<menor:
            menor=lista[c]
print(f'Os números da lista são: {lista}')
print(f'O maior valor é {maior} na posição...', end='')
for i,v in enumerate(lista):
    if v==maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor é {menor} na posição...', end='')
for i,v in enumerate(lista):
    if v==menor:
        print(f'{i}...', end='')

