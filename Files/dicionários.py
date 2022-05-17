'''pessoas={'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
#del pessoas['sexo']
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    #pessoas.items vai substituir o ennumarate
    print(f'{k} = {v}')
pessoas['nome']= 'Guts'
pessoas['peso']= 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
brasil=[]
estado1= {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2= {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['sigla']) '''

estado = dict()
brasil= list()
for c in range(0,3):
    estado['uf']= str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    #brasil.append(estado['uf'])
    #brasil.append(estado['sigla'])
    brasil.append(estado.copy()) #Cópia do dicionário
for e in brasil:
    for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
        print(v)
        