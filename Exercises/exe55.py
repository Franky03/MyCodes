maior=0
menor= 0
for c in range(1, 6):
   peso= float(input('Qual o peso da {}ª pessoa ?'.format(c)))
   if c==1:
      maior= peso
      menor= peso
   else:
        if peso> maior:
            maior= peso
        if peso<menor:
            menor= peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor)) 
