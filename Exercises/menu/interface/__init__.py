def leiaInt(numero):
    ok= False 
    valor=0 
    while True:
        try:
            n= int(input(numero))
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

def linha(tam=42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc= leiaInt('Sua opção: ')
    return opc