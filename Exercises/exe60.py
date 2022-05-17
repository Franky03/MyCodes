num= int(input('Digite um número para seu fatorial: '))
c= num
f=1
print('Calculando {}!...'.format(num))
while c>0:
    print(c, end= '')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f)