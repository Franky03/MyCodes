c=n=s=0
while True:
    n= int(input('Digite um número: '))
    if n==999:
        break
    s+=n
    c += 1
print(f'A soma dos {c} números é {s} ')