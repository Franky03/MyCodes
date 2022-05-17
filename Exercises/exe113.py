def leiaInt(numero):
    ok= False 
    valor=0 
    while True:
        try:
            n= int(input(numero)).strip()
        except(ValueError,TypeError):
            print('ERRO!O tipo de dado está errado.')
        except KeyboardInterrupt:
            print('ERRO!O usuário não informou os dados.')
            return 0
        else:
            valor=n
            ok=True
        if ok:
            break 
    return valor

def leiaFloat(numero):
    valor=0
    ok= False
    while True:
        try:
            n= float(input(numero)).strip()
        except(ValueError, TypeError):
            print('ERRO!O tipo de dado está errado.')
        except KeyboardInterrupt:
            print('ERRO!O usuário não informou os dados.')
            return 0
        else:
            valor=n
            ok=True
        if ok:
            break
    return valor

n= leiaInt('Digite um número: ')
f= leiaFloat('Digite um número real: ')
print(f'Voce digitou os números {n} e {f}')
