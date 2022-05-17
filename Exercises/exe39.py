ano= int(input('Quantos anos tem a pessoa? '))
falta= 18-ano
passou= ano-18
if ano<18:
    print('Vc ainda vai se alistar daqui a {} ano(s)'.format(falta))
elif ano>18:
    print('Vc já deveria ter se alistado há {} ano(s)'.format(passou))
else:
    print('Está no tempo de se alistar')
#40
nt1= float(input('Nota 1: '))
nt2= float(input('Nota 2: '))
media= (nt1+nt2)/2
if media>= 7.0:
    print('Aprovado')
elif 5.0 < media < 6.9:
    print('Recuperação')
elif media<5.0:
    print('Reprovado')
#41
import time as tm
idade= int(input('Qual a idade do nadador? '))
print('Categoria...')
tm.sleep(1)
if idade<=9:
    print('Mirim')
elif 9<idade<=14:
    print('Infantil')
elif 14<idade<=19:
    print('Junior')
elif idade==20:
    print('Senior')
else:
    print('Master')
#43
peso= float(input('Peso: '))
altura= float(input('Altura: '))
imc= peso/(altura**2)
print('Seu IMC é {:.1f}'.format(imc),'e vc está na categoria', end=' ')
if imc<18.5:
    print('Abaixo do peso')
elif 18.5<= imc <25:
    print('Peso ideal')
elif 25<= imc <30:
    print('Sobrepeso')
elif 30<= imc <40: 
    print('Obesidade')
else:
    print('Obesidade mórbida')