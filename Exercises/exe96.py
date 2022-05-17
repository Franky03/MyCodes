def linha(n):
    print('-='*n)

def área(larg, compr):
    area= larg*compr
    print(f'A área de um terreno de {l}x{c} é de {area:.2f}m2')

def volume(*valores):
    #vlme= larg * compr * altura
    v=1
    for num in valores:
        v *= num
    print(f'O volume do cubo {valores} é de {v:.2f}m3')

linha(20)
l= float(input('Largura(m): '))
c= float(input('Comprimento(m): '))
h= float(input('Altura(m): '))
área(l,c)
volume(l, c, h)
linha(20)