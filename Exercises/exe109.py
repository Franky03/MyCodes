import moeda109
valor= float(input('Digite um valor: R$'))
print(f'Aumentando 20% de {moeda109.conv(valor)}, temos R${moeda109.aumentar(valor, 20, True)}')
print(f'Diminuindo 15% de {moeda109.conv(valor)}, temos R${moeda109.diminuir(valor,15, True)}')
print(f'O dobro de {moeda109.conv(valor)} é R${moeda109.dobro(valor,True)}')
print(f'A metade de {moeda109.conv(valor)} é R${moeda109.metade(valor)}')