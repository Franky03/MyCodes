#for c in range(7, 0, -1): #do maior para o menor
    #print(c)
#for n in range(0, 10, 2): #pulando de 2 em 2
    #print(n)
i=int(input('Inicio: '))
f= int(input('Fim: '))
p= int(input('passo:'))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#...
s=0
for c in range(0, 4):
    n= int(input('Digite um nmr:'))
    s+=n
print('{}'.format(s))