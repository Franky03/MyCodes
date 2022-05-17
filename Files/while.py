from re import S


c=1
while c<10:
    print(c, end=' ')
    c+=1
print('Fim')
n=1
r= 'S'
contpar=0
contin=0
while n !=0:
    n=int(input('Dgt um nmr: '))
    if n !=0 :
        if n%2==0:
            contpar += 1
        else:
            contin += 1

print('números pares {} e ímpares {}'.format(contpar, contin))