temp=[[], []]
valor=0
for c in range(0, 7):
    valor= (int(input('Número: ')))
    if valor%2==0:
        temp[0].append(valor)
    else:
        temp[1].append(valor)
temp[0].sort()
temp[1].sort()
print(f'A lista par crescente é: {temp[0]}')
print(f'A lista impar crescente é: {temp[1]}')