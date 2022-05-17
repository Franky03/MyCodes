palavra1= str(input('Primeira palavra: ')).strip()
palavra2= str(input('Segunda palavra: ')).strip()
if palavra1== (palavra2[::-1]) :
    print('A palavra É INVERSA')
else:
    print('A palavra NÃO É INVERSA')