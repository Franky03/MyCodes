total=totmil=menor=cont=0
barato=''
while True:
    produto=str(input('Produto: '))
    preço= float(input('Preço: R$'))
    cont +=1
    total += preço
    if preço>1000:
        totmil +=1
    if cont==1 or preço<menor :
        menor=preço
        barato = produto
    resp= ' '
    while resp not in 'SsNn':
        resp= str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        print('Detectou')
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {totmil} produtos que custam mais de 1000 reais')
print(f'O produto mais barato é {barato} e custa R${menor}')
