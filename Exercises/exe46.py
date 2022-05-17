from time import *
for c in range(10, 0, -1):
    print(c)
    sleep(1)
#for b in range(2, 52, 2): #pares de dois em dois entre 1 e 50, começa pelo 2 termina em 52 pq só vai contar o 50
    #print(b)
s=0
co= 0
for a in range(1 ,501, 2):
    if a%3 ==0:
        co = co +1
        print(a)
        s+=a
print('foram encontrados {} números e a soma deles é {}'.format(co, s))