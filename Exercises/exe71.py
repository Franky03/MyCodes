print('='*30)
print('Banco')
print('='*30)
c50=c20=c10=c1=0
valor=int(input('Digite o valor do saque: R$'))
if valor>=50:
    while True:
        c50 += 1
        valor -= 50
        if valor<50:
            break
if valor>=20:
    while True:
        c20 += 1
        valor -=20
        if valor<20:
            break
if valor>=10:
    while True:
        c10 +=1
        valor -= 10
        if valor <10:
            break
if valor>=1:
    while True:
        c1+=1
        valor -= 1
        if valor<1:
            break
print('Vc receberá')
if c50>0:
    print(f'{c50} notas de R$50,00')
if c20>0:
    print(f'{c20} notas de R$20,00')
if c10>0:
    print(f'{c10} notas de R$10,00')
if c1>0:
    print(f'{c1} notas de R$1,00')
