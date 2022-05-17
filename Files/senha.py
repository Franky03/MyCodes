import random
import time

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '[]{}()*#;/,-_%'

qnt= 8
qntInt = int(qnt)
length= qntInt

#All= lower + upper + digits +symbols
#passwordAll = "".join(random.sample(All, length))
Maxnum=  upper + digits 
passwordMaxnum = "".join(random.sample(Maxnum, length))

print('Processando senha...')
time.sleep(3)
print('Sua senha é = ' + passwordMaxnum)
#print('passwordAll = ' + passwordAll)
time.sleep(5)
print('Tenha um bom dia')