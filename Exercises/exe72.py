números= ('zero','um', 'dois',
'três', 'quatro', 'cinco', 'seis', 'sete',
'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
num= (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
while True:
    n= int(input('Digite um número de 0 a 20 (999 para parar) :'))
    if n in num :
        print(f'você escolheu o número {números[n]}')
        if n==999:
            break
    elif n not in num and n!=999:
        print('Número inválido')
    elif n==999:
        print('FIM')
        break
