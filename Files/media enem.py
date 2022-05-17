h= float(input('Humanas'))
l= float(input('Linguagens'))
n= float(input('Natureza'))
m= float(input('Matemática'))
r= float(input('Redação'))
#soma= h+l+n+m+r
#media= soma/5
soma= (l*1.5+m*1.0+h*1.5+n*3.0+r*1.5)
mp=(soma/8.5)
pond= mp*1.2
print ('Sua média ponderada é{:.2f}'.format(pond))

