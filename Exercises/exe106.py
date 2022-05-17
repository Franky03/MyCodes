from time import sleep
def ajuda(com):
    help(com)

def titulo(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


while True:
    titulo('SISTEMA DE AJUDA')
    hp= str(input('Função ou biblioteca >'))
    if hp.upper() == 'FIM':
        break
    else:
        print(f"Acessando o manual de comando '{hp}'...")
        sleep(2)
        print('~~'*30)
        ajuda(hp)
print('FINALIZADO')




