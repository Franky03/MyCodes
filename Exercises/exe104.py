def leiaInt(numero):#Número vai ser a mensagem do input
    ok= False #Uma variável para verificar se está ok
    valor=0 #O valor que vai ser retornado
    while True:
        n= str(input(numero)) #Vai ler como uma string para converter caso for numerico
        if n.isnumeric(): #Se o input de n for um número inteiro...
            valor= int(n) #...o valor vai ser o inteiro de n
            ok= True #Ok vai ser verdadeiro pois o valor é inteiro
        else:
            print('ERRO! Digite um número inteiro!')
        if ok:
            break 
    return valor

n= leiaInt('Digite um número: ')
print(f'Voce digitou o número {n}')
