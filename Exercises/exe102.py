def fatorial(num, show=False):
    f=1
    for c in range(num, 0, -1):
        f *= c
        if show==True:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
while True:
    n= int(input('Número para fatorial: '))
    if n==0:
        break
    print(fatorial(n, True))