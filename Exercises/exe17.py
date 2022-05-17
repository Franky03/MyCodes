from math import radians, sin, cos, tan, hypot
#Hipotenusa
co= float(input('Comprimento do cateto oposto'))
ca= float(input('Comprimento do cateto adjacente'))
h= hypot(co, ca)
print('A hipotenuza vai medir {:.2f}'.format(h))
#sen e cos
ang= float(input('Digite um angulo'))
sen= sin(radians(ang))
cos= cos(radians(ang))
tg= tan(radians(ang))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang,sen,cos,tg))
#sortear um iten
import random
a1= str(input('Aluno 1'))
a2= str(input('Aluno 2'))
a3= str(input('Aluno 3'))
a4= str(input('Aluno 4'))
lista= [a1, a2, a3, a4]
sort= random.choice(lista)
print('O aluno sorteado foi {}'.format(sort))
#sortear ordem
random.shuffle(lista)
print('A ordem de apresentação será ',end='')
print(lista)
