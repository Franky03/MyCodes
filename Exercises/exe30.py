num= int(input('Digite um número: '))
result= num % 2 #O resto da divisão do numero por 2
if result==0:
    print('O número é Par')
else:
    print('O número é Impar')  
#...
d= float(input('Qual a distancia da viagem? '))
if d<=200:
    custo= d*0.50
else:
    custo= d*0.45
print('Vc vai pagar {:.2f} reais pela viagem.'.format(custo))
#...
import time
from datetime import date
ano= int(input('Qual ano vc quer analisar ? Coloque 0 para analisar o ano atual')) 
if ano==0:
    ano= date.today().year
print ('Analisando...')
time.sleep(2)
if ano % 4==0 and ano % 100 != 0 or ano % 400==0:
    print ('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
#...
a= int(input('Primeiro número: '))
b= int(input('Segundo número: '))
c= int(input('Terceiro número: '))
menor = a
if  b<a and b<c:
    menor= b
if c<a and c<b:
    menor= c
print('O menor número é {}'.format(menor))
maior= a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior= c
print('O maior número é {}'.format(maior))




