#Analisador completo
somaidade= 0
mi=0
maior_hom=0
nomevelho=0
muievint=0
for p in range(1, 5):
    print('-'*5, ' {} PESSOA '.format(p), '-'*5)
    nome= str(input('Nome: ')).strip()
    idade= int(input('Idade: '))
    sexo= str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p==1 and sexo in 'mM':
        maior_hom= idade
        nomevelho= nome
    if sexo in 'mM' and idade>maior_hom:
        maior_hom=idade
        nomevelho=nome
    if sexo in 'Ff' and idade < 20:
        muievint += 1
mi= somaidade/4
print('A média das idades é {}'.format(mi))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_hom, nomevelho))
print('Ao todo tem {} mulheres com menos de 20 anos'.format(muievint))