from math import sqrt


n= input("Numero de unidades da célula unitária: ")
Ac= sum(int(str(input("Pesos atomicos dos cátions da celula: ")).split(' ')))
Aa= sum(input("Pesos atomicos dos anions da celula: ").split(' '))
raio= input('Raio ou Volume da celula unitária')
NA= 6.023* 10e23

aresta= 2* raio * sqrt(2)
volume = pow(aresta, 3)

densidade= n*(Ac + Aa)/ volume * NA

print(densidade)