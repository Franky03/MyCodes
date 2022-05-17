lista=[]
while True:
    num=int(input('Digite um número:'))
    if num not in lista:
        lista.append(num)
    elif num in lista:
        print("Número já está na lista")
    fim= str(input('Quer continuar ? [N para parar]')).upper().strip()[0]
    if fim in 'Nn':
        break
lista.sort()
print(f'A lista digitada foi: ', end='')
for c in lista:
    print(c, end=' ')