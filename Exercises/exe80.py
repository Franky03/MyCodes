lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n> lista[-1]:
        lista.append(n)
        print("Adicionado na ultima posição...")
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
print(f' A lista em ordem é : {lista}')