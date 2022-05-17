def aumentar(moeda=0, pct=0):
    return moeda + (moeda* (pct/100))

def diminuir(moeda=0, pct=0):
    return moeda - (moeda* (pct/100))

def dobro(moeda=0):
    return moeda*2

def metade(moeda=0):
    return moeda/2

#Exercicio 108
def moeda(preço= 0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
