tupla=(int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print('Os valores são: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu a primeira vez na {tupla.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados são: ', end='')
for c in tupla:
    if c%2==0:
        print(c, end=' ')