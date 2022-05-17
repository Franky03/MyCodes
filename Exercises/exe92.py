from datetime import datetime
dici= dict()
dici['Nome']= str(input('Nome: '))
dici['Idade']= datetime.now().year - int(input('Ano de nascimento: '))
dici['CTPS']= int(input('Carteira de trabalho(0 não tem): '))
if dici['CTPS']==0:
    print('-='*25)
    for k, v in dici.items():
        print(f'- {k}: {v}')
else:
    dici['Contratação']= int(input('Ano de contratação: '))
    dici['Salário']= float(input('Salário: R$'))
    dici['Aposentadoria']= dici['Idade'] + ((dici['Contratação']+35) - datetime.now().year)
    print('-='*25)
    for k,v in dici.items():
        print(f'- {k}: {v}')
