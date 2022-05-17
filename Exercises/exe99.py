from time import sleep
listam=[]

def linha(n):
    print('-='*n)

def maior(*num):
    linha(20)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
        listam.append(v)
    print(f'Foram informados {len(num)} valores ao todo.')
    maior=0
    for c in listam:
        if c==0:
            maior=c
        else:
            if c>maior:
                maior=c
    print(f'O maior valor informado foi {maior}.')
    listam.clear()

maior(2,6,15,8,12,20,4)
maior(5,5,5)
maior(2,5,9)
maior(5,7)
maior(6)
maior()