matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):#para cada linha in range de 0 a 2
    for c in range(0,3): #para cada coluna in range de 0 a 2
        matriz[l][c]=int(input(f'Valor para [{l}, {c}]: '))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()