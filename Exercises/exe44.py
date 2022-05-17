print('{:=^40}'.format(' LOJA ESPARTANS '))
valor= float(input('Qual o valor da compra: R$'))
print(''' FORMA DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op= int(input('Qual a opção ?'))
if op==1:
    print('Você pagará R${:.2f} pela compra, com 10% de desconto'.format(valor*0.9))
elif op==2:
    print('Você pagará R${:.2f} pela compra, com 5% de desconto'.format(valor*0.95))
elif op==3:
    parcela= valor/2
    print('Você não tem desconto e pagará R${} em 2 parcelas de R${}'.format(valor, parcela))
elif op==4:
    vf= (valor*1.2)
    quant= int(input('Em quantas parcelas?'))
    parcela= vf/quant
    print('Você pagará R${:.2f}, com 20% de juros, em {} parcelas de R${}'.format(vf, quant, parcela))
else:
    print('Não existe essa opção')