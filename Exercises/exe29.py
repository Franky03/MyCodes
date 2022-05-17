v= float(input('Qual a velocidade do carro? '))
multa= 7*(v-80.0)
if v>80:
    print('Vc foi multado e terá que pagar {} reais'.format(multa))
else:
    print('Ta no limite, continue assim!!')