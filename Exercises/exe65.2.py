#Colocar uma variável de iniciação
from statistics import median
from numpy import quantile


resp='S'
#criar as variáveis
soma=quant=media=maior=menor=0
#criar o while
while resp in 'Ss':
    num= int(input('Digite um número: '))
    soma += num
    quant +=1
    resp= str(input('Quer continuar ? [S/N]'))
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior = num
        if num<menor:
            menor=num
media=soma/quant
print(quant, media, maior, menor)