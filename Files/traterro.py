opc=0
while True:
    x= int(input('Digite X:'))
    y= int(input('Digite Y: '))
    soma= x * y
    print(f'{x} X {y} = {soma}')
    print('[0]Multiplicar\n[1]Sair\n')
    opc= int(input('Escolha: '))
    if opc==1:
        break
