import math
matriz=[[0,0,0],[0,0,0],[0,0,0]]
maior=soma=spares=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        #soma= matriz[l][2] + matriz[l][2] não está errado, mas tem um jeito mais simplificado
        if matriz[l][c]%2==0:
            spares += matriz[l][c]
    print()
for l in range(0,3):
    soma += matriz[l][2]
for c in range(0,3):
    if c==0:
        maior= matriz[1][c]
    elif matriz[1][c]>maior:
        maior= matriz[1][c]
print(f'A soma dos pares é {spares}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior numero da segunda linha é {maior}')