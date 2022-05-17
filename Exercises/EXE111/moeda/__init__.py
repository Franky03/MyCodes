def aumentar(moeda=0, pct=0, formato=False):
    resp= moeda + (moeda* (pct/100))
    return resp if formato is False else conv(resp)

def diminuir(moeda=0, pct=0, formato=False):
    resp= moeda - (moeda* (pct/100))
    return resp if formato is False else conv(resp)

def dobro(moeda=0, formato=False):
    resp= moeda*2
    return resp if formato is False else conv(resp)

def metade(moeda=0, formato=False):
    resp= moeda/2
    return resp if formato is False else conv(resp)

#Exercicio 108
def conv(preço= 0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

#Exercício 109
def resumo(moeda=0, pcta=10, pctd=5):
    print('-'*37)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*37)
    print(f'{"Valor analisado:":<5}\t{conv(moeda)}') #\t serve para tabulação, como se fosse :>20
    print(f'{"Dobro do preço: ":<5}\t{dobro(moeda,True)}')
    print(f'{"Metade do preço:":<5}\t{metade(moeda, True)}')
    print(f'{pcta}','%',f'{"de aumento:":<5}\t{aumentar(moeda, pcta, True)}')
    print(f'{pctd}','%',f'{"de redução:":<5}\t{diminuir(moeda, pctd, True)}')
    print('-'*37)
