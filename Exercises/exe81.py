lista=[]
def lin():
    print('=='*15)
while True: 
    n=int(input('Digite um valor: '))
    lista.append(n)
    resp=str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
lista.sort(reverse=True)
lin()
print(f'Vc digitou {len(lista)} números')
print(f'A lista em ordem decrescente é:  {lista}')
if 5 in lista:
    print(f'O valor 5 aparece {lista.count(5)} vezes na lista')
else:
    print('O número 5 não aparece na lista')
lin()