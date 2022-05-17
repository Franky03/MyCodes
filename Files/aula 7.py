n1= int(input('Digite um número'))
n2= int(input('Digite outro'))
n3= int(input('Digite um valor em metros'))
n4= int(input('Número'))
real= float(input('Quantos reais vc tem?'))
larg=float(input('Qual a largura da parede?'))
alt=float(input('Qual a altura da parede?'))
preço=float(input('Qual o preço do produto?'))
salar= float(input('Qual seu salário atual?'))
new= salar*1.15
desc= preço*0.95
ar= larg*alt
tint= ar/2
dolar= real/5.09
soma= n1+n2
media= soma/2
#m= n1*n2
#p= n1**n2
#print('A soma dos números é {} e a divisão é {}'.format(soma, d), end='')
#print('A multiplicação é {} e a potencia é {}'.format (m, p))
print('O antecessor de {} é'.format(n1),(n1-1),'e o seu sucessor é{}'.format(n1+1))
print('O dobro de {} é'.format(n1), (n1*2),',o seu triplo é{}'.format(n1*3), 'e sua raiz quadrada é{:.2f}'.format(n1**(1/2)))
print('A média de {} e{} é {}'.format(n1,n2,media))
print('{} metros contém {}centimetros e {}milimetros'.format(n3,(n3*100),(n3*1000)))
print('A tabuada de {} é:{} {} {} {} {} {} {} {} {} {}'.format(n4,(n4*1),(n4*2),(n4*3),(n4*4),(n4*5),(n4*6),(n4*7),(n4*8),(n4*9),(n4*10)))
print('Vc tem {} reais, então vc tem {:.2f} dolares'.format(real,dolar))
print('A área da parede é {} e precisa de {} baldes de tinta para pintá-la'.format(ar,tint))
print('O produto de valor{} fica por {} com o desconto'.format(preço,desc))
print('Seu novo salário será de {:.2f} reais'.format(new))
