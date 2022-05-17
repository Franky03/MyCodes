def leia(money):
    while True:
        moeda= str(input(money)).replace(',','.').strip()
        ok= False
        if moeda.isalpha() or moeda == '':
            print(f'ERRO: \"{moeda}\" é um valor inválido!')
        else:
            ok=True
            return float(moeda)
        if ok:
            break
