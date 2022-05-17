import moeda
valor= float(input('Digite um valor: R$'))
print(f'Aumentando 20% de R${valor}, temos R${moeda.aumentar(valor, 20)}')
print(f'Diminuindo 15% de R${valor}, temos R${moeda.diminuir(valor,15)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'A metade de R${valor} é R${moeda.metade(valor)}')