import random
from time import sleep
comput= random.randint(0,5)
print('---='*10)
print('Vou pensar em um número de 0 a 5. Tente adivinhar....')
print('---='*10)
num=int(input('Em que número eu pensei? '))
print('Processando...')#demora um tempo com o time.sleep()
sleep(3)
if num==comput:
    print('eu pensei no número {} e vc no numero {}'.format(comput, num))
    print('Voce acertou')
else:
    print('Eu pensei em {} e vc em {}'.format(comput, num))
    print('Vc errou')
