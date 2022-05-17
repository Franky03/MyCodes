frase= str(input('Digite a frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= junto[::-1]
#for letra in range(len(junto) - 1, -1, -1):
    #inverso += junto[letra]
print(junto, inverso)
if junto==inverso:
    print('É um palíndromo')
else:
    print('Não é palíndromo')
