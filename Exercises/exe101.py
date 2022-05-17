from datetime import date
def linha():
    print('-='*25)

def voto(idade):
    linha()
    print(f'A pessoa tem {idade} anos e seu voto é ', end='')
    if idade>=18:
        return 'OBRIGATÓRIO!!'
    elif idade<18 and idade>=16 or idade>65:
        return 'OPCIONAL!!'
    else:
        return 'NEGADO!!'
    
atual= date.today().year
while True:
    nasci =int(input('Ano de nascimento: '))
    if nasci<=1890:
        resp= str(input('Essa data é muito antiga, tem certeza? [S/N]')).upper().strip()[0]
        if resp in 'Ss':
            break
    elif nasci> atual:
        print('Essa ano é inválido, digite novamente')
    else:
        break

ano= atual- nasci
print(voto(ano))