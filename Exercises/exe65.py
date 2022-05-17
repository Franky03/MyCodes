resp= 'S'
soma=quant=média=maior=menor=0
while resp in 'Ss':
    num=int(input('Digite um número: '))
    soma += num
    quant +=1
    resp= str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quant==1:
        menor=menor=num
    else:
        if num> maior:
            maior=num
        if num<menor:
            menor=num
média=soma/quant
print(f'vc digitou {quant} números e a média foi {média}')
print(f'O maior número é {maior} e o menor é {menor}')