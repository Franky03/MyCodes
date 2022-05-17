maior=0
homem=0
mulher20=0
while True:
    print('=='*20)
    idade= int(input('Idade da pessoa: '))
    sexo= str(input('Sexo da pessoa [M/F]:')).strip().upper()[0]
    print('=='*20)
    escolha= str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('=='*20)
    if escolha in 'Ss':
        if idade>18:
            maior += 1
        if sexo in 'Ff' and idade<20:
            mulher20 +=1 
        if sexo in 'Mm':
            homem+=1
    elif escolha in 'Nn':
        if idade>18:
            maior += 1
        if sexo in 'Ff' and idade<20:
            mulher20 +=1 
        if sexo in 'Mm':
            homem+=1
        break
    elif escolha not in 'MmFf':
        print('Opção inválida, tente novamente')
print(f'Ao todo, são {maior} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'Foram cadastradas {mulher20} mulheres com menos de 20 anos')