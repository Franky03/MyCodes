tabela=('Lápis', 1.50 ,'Caderno', 25, 'Borracha', 2, 'Carne', 125, 'Mochila', 98.50, 'Faca', 26, 'G18', 350, 'Ponta Grafite', 4,
'AK47', 56)
print('='*40)
print(f'{"MATERIAL ESCOLAR":^40}')
print('='*40)
for pos in range(0, len(tabela)):
    if pos%2==0:
        print(f'{tabela[pos]:.<30}', end='')
    else:
        print(f'R${tabela[pos]:>7.2f}')
print('='*40)