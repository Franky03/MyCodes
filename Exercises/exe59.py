from time import *
n1= int(input('Digite o primeiro número número: '))
n2= int(input('Digite o segundo número: '))
opção=0
while opção !=5:
    print('=='*5, 'MENUZIN', '=='*5)
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    opção= int(input('Qual a sua opção? '))
    if opção==1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
    elif opção==2:
        print('A multiplicação de {} com {} é {}'.format(n1, n2, n1*n2))
    elif opção==3:
        if n1>n2:
            print('O maior número é {}'.format(n1))
        if n2>n1:
            print('O maior número é {}'.format(n2))
        else: 
            print('Os números são iguais')
    elif opção==4:
        print('Diga aí meu patrão')
        n1= int(input('Digite o novo número: '))
        n2= int(input('Digite outro valor: '))
    elif opção==5:
        print('Até mais meu joia')
    else:
        print('Opção inválida')
    sleep(2)
print('Fim do programa')
