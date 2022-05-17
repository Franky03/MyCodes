#n=int(input('Número para sua tabuada: '))
#for c in range(0,11):
    #print(n*c)
s=0
cont=0
#for b in range(1,7):
    #numb= int(input('Digite o {}° valor:'.format(b))) 
    #if numb % 2==0:
       # s += numb
        #cont += 1
#print('São {} números pares e a soma deles é {}'.format(cont, s))
print('=='*10, ' PRIMEIROS 10 TERMOS DE UMA PA ', '=='*10)
pt= int(input('Primeiro termo: '))
ra= int(input('Razão: '))
dec= pt + (10-1)*ra
for a in range(pt, dec + ra, ra):
    print(a, end='-')
print('FIM')
