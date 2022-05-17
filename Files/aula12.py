#ex36
casa= float(input('Qual o valor da casa?'))
salário= float(input('Qual o seu salário?'))
anos= float(input('Em quantos anos vc quer pagar?'))
mes= anos*12
parcela= casa/mes
if parcela <= (salário*0.3):
    print('A sua parcela é de {:.2f} reais.'.format(parcela)) 
elif parcela > (salário*0.3):
    print('O empréstimo foi negado')
#ex38
num1= int(input('Digite um número: '))
num2= int(input('Digite outro: '))
if num1>num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1<num2:
    print('{} é maior que {}'.format(num2, num1))
else:
    print('Os números são iguais')
