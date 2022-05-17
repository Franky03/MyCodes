num=cont=0
while True:
    num= int(input('Qual número vc quer ver a tabuada? '))
    if num<0:
        break
    for c in range(1,11):
        tabuada= num*c
        print(f'{num} X {c} = {tabuada}')
print('Acabou a tabuada')