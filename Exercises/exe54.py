contmaior=0
contmenor=0
for c in range(1,8):
    ano= int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade= 2022-ano
    if idade>=18:
        contmaior += 1
    else:
        contmenor += 1
print ('Tivemos {} pessoas maior de idade e {} pessoas menor de idade'.format(contmaior, contmenor))
