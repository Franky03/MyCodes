brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f'A tabela do brasileirão é: {brasileirão}')
print('=='*20)
print(f'Os cinco primeiros times da tabela são: {brasileirão[0:5]}')
print('=='*20)
print(f'A ordem alfabética dos times é: {sorted(brasileirão)}')
print('=='*20)
chape=brasileirão.index('Chapecoense') + 1
print(f'A chapecoense está na {chape}° posição')
print('=='*20)
print(f'Os  últimos quatro times são: {brasileirão[-4:]}')