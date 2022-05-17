lista= []
pessoa= {}
soma=0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('Sexo [M/F]: ').strip().upper()[0])
        if pessoa['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Digite apenas M ou F')
    pessoa['idade']= int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        conti= str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if conti in 'SsNn':
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if conti in 'Nn':
        break
print(lista)
print('=-'*30)
print(f'A) Foram cadastradas {len(lista)} pessoas')
media= soma/len(lista)
print(f'B) A média das idades é: {media:.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']} ", end='')
print()
print('D) As pessoas acima da média são: ', end='')
for p in lista:
    if p['idade']>= media:
        print('    \n')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('FIM')
