import random
'''valores=[]
for c in range(0,10):
    c=random.randint(0,100)
    if c%2==0:
        valores.append(c)
print(valores)'''

'''lista=[8, 9, 3, 4]
print(lista)
lista.append(5)
print(lista)
lista.insert(3, 15)
print(lista)
del lista[2]
print(lista)
lista.pop(2)
print(lista)
lista.pop() #vai apagar o último
print(lista)
print(len(lista))
valor= list(range(0,7))
print(valor)
valor.sort(reverse=True)
print(valor)'''
mais=[]
'''while len(mais) != 8:
    mais.append(random.randint(0,100))
for c,v in enumerate(mais):
    print(f'Na posição {c}, encontrei o número {v}')
print('Cheguei no final da lista')'''
teste= list()
teste.append('Paulo')
teste.append(29)
galera= []
galera.append(teste[:])
teste[0]='Maria'
teste[1]= 25
galera.append(teste[:])
print(galera)
nogale= [['Luke', 15], ['Joke', 16], ['Lati', 20], ['Kate', 22]]
print(nogale[0])
print(nogale[0][0])
print(nogale[1][0])
print(nogale[2][1])
for p in nogale:
    print(f'{p[0]} tem {p[1]} anos de idade')
nova= list()
dados= list() #Lista auxiliar para adicionar em nova
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    nova.append(dados[:])
    dados.clear()
print(nova)
totma=0
totme=0
for p in nova:
    if p[1]>20:
        print(f'{p[0]} é maior de idade e tem {p[1]} anos')
        totma+=1
    else:
        print(f'{p[0]} é menor de idade e tem {p[1]} anos')
        totme+=1
print(f'Temos {totma} maiores e {totme} menores')