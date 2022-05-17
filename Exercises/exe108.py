import moeda
valor= float(input('Digite um valor: R$'))
print(f'Aumentando 20% de {moeda.moeda(valor)}, temos R${moeda.moeda(moeda.aumentar(valor, 20))}')
print(f'Diminuindo 15% de {moeda.moeda(valor)}, temos R${moeda.moeda(moeda.diminuir(valor,15))}')
print(f'O dobro de {moeda.moeda(valor)} é R${moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é R${moeda.moeda(moeda.metade(valor))}')