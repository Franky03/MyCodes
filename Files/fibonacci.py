n= int(input('Quantos termos vc quer ver? '))
t1=0
t2=1
cont=3
print(f'{t1} - {t2}', end= ' ')
while cont<=n:
    t3= t1+t2
    print(f'- {t3}', end=' ')
    t1=t2
    t2=t3
    cont += 1
#Quando o t3 for executado, o t1 vai ser o t2 e o t2 vai ser o t3 para um novo t3 ser formado

    