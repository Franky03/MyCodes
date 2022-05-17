nomes= []
for c in range(1,4):
    nome=str(input('{}° nome: '.format(c)))
    idade= int(input('Sua idade: '))
    if idade==21:
        nomes.append(nome)
print(nomes)
