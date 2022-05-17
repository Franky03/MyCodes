from time import sleep

def linha():
    print('-='*20)

def contador(ini, fim, passo):
    if passo<0:
        passo *= -1
    if passo==0:
        passo=1
    linha()
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(2)
    if ini<fim:
        c=ini
        while c <= fim:
            print(f'{c} ', end='', flush=True)
            c += passo
            sleep(0.5)
        print('FIM !')
    else:
        c= ini
        while c>=fim:
            print(f'{c} ', end='', flush=True)
            c -= passo
            sleep(0.5)
        print('FIM !')

contador(1,10,1)
contador(10,0,2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i= int(input('Início: '))
f= int(input('Fim: '))
p= int(input('Passo: '))
contador(i,f,p)