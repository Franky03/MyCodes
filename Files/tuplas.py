lanche= ('hambúrguer', 'suco', 'pizza', 'pudim')
#TUPLAS SÃO IMÚTAVEIS
#lanche[1]= 'Refri'
'''print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])
print(lanche[-2:])'''
print(len(lanche))
'''for cont in range(0, len(lanche)):
    print(f'eu comi muito {lanche[cont]}') 
for comida in lanche:
    print(f'eu comi muito{comida}')
for pos, comida in enumerate(lanche):
    print(f'eu comi muito {comida} na posição {pos}')
print(sorted(lanche))#Colocar a tupla em ordem'''

a=(2, 5, 4)
b=(5, 8, 1, 2)
c= a+b
print(c)
len(c)
print(c.count(5))
print(c.count(9))
print(c.index(4))